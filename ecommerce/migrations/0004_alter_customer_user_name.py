# Generated by Django 4.2.5 on 2023-10-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_remove_customer_phone_alter_products_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
