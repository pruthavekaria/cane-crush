from django.db.models import Case, IntegerField, Value, When
from django.db.models.functions import Cast, Replace
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, OrderItem
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Order, OrderItem
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    products = Product.objects.all()
    rating_range = range(5)
    context = {
        "products": products,
        "rating_range": rating_range
    }
    return render(request, 'shop.html', context)


def product_view(request, slug):
    if request.method == "POST":
        selected_product_name = request.POST.get('selected_product_name')
        selected_discounted_price = request.POST.get('selected_discounted_price')
        selected_original_price = request.POST.get('selected_original_price')
        selected_pack_size = request.POST.get('selected_pack_size')
        print(selected_discounted_price)
        print(selected_original_price)
        print(selected_pack_size)
        print(selected_product_name)
        product = Product.objects.get(name=selected_product_name)

        order = Order.objects.create(customer=request.user, paid=False)
        if selected_discounted_price:
            OrderItem.objects.create(order=order, product=product, quantity=1, price=selected_discounted_price)
        else:
            OrderItem.objects.create(order=order, product=product, quantity=1, price=selected_original_price)
        return redirect('cart')

    product = get_object_or_404(Product, slug=slug)
    pack_sizes = product.pack_size.all()
    ordered_pack_sizes = product.pack_size.annotate(
        numeric_size=Case(
            When(size__icontains='kg', then=Cast(Replace('size', Value('kg'), Value('')), IntegerField()) * 1000),
            When(size__icontains='g', then=Cast(Replace('size', Value('g'), Value('')), IntegerField())),
            output_field=IntegerField()
        )
    ).order_by('numeric_size')

    context = {
        'product': product,
        'pack_sizes': pack_sizes,
        'ordered_pack_sizes': ordered_pack_sizes
    }

    return render(request, 'product-view.html', context)


def view_cart(request):
    orders = Order.objects.filter(customer=request.user)
    cart_items = OrderItem.objects.filter(order__in=orders)

    total_amount = sum(item.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_amount': total_amount
    }

    return render(request, 'cart.html', context)


def remove_item_from_cart(request, id):
    cart_item = get_object_or_404(OrderItem, id=id)
    cart_item.delete()
    return redirect('cart')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = f"New contact message from {form.cleaned_data['fname']} {form.cleaned_data['lname']}"
            message = f"From: {form.cleaned_data['fname']} {form.cleaned_data['lname']} <{form.cleaned_data['email']}>\n\nMessage:\n{form.cleaned_data['message']}"
            sender_email = form.cleaned_data['email']
            recipient_list = ['axayqa1221@gmail.com']
            send_mail(subject, message, sender_email, recipient_list)
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def blog(request):
    return render(request, 'blog.html')
