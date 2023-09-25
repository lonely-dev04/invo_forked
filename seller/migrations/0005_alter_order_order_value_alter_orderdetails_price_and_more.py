# Generated by Django 4.2.4 on 2023-09-25 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_order_completed_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_value',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
