# Generated by Django 4.2.13 on 2024-08-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryManagementApp', '0002_product_stocklevel_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(default=0, max_length=255, unique=True),
        ),
    ]
