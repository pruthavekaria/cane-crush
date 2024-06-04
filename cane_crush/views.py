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
        selected_pack_size = request.POST.get('selected_pack_size')
        print(selected_pack_size)

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
    print("context :-", context)
    return render(request, 'product-view.html', context)


def view_cart(request):
    cart_items = OrderItem.objects.all()
    total_amount = sum(item.total_price for item in cart_items)
    context = {
        'cart_items': cart_items, 'total_amount': total_amount}

    return render(request, 'cart.html', context)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = f"New contact message from {form.cleaned_data['fname']} {form.cleaned_data['lname']}"
            message = f"From: {form.cleaned_data['fname']} {form.cleaned_data['lname']} <{form.cleaned_data['email']}>\n\nMessage:\n{form.cleaned_data['message']}"
            sender_email = form.cleaned_data['email']
            recipient_list = ['mailto:axayqa1221@gmail.com']
            send_mail(subject, message, sender_email, recipient_list)
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

