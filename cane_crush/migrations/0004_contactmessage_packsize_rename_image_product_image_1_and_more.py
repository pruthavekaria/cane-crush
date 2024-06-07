# Generated by Django 4.2.13 on 2024-06-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cane_crush', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PackSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, choices=[('250g', '250 grams'), ('500g', '500 grams'), ('1kg', '1 kilogram'), ('2kg', '2 kilograms'), ('5kg', '5 kilograms')], max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image_1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='original_price',
        ),
        migrations.AddField(
            model_name='product',
            name='discount_percentage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='product',
            name='pack_size',
            field=models.ManyToManyField(blank=True, related_name='products', to='cane_crush.packsize'),
        ),
    ]
