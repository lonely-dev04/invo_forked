# Generated by Django 4.2.4 on 2023-09-06 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customer_address_pin_shop_joined_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
