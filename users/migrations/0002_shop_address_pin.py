# Generated by Django 4.2.4 on 2023-09-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address_pin',
            field=models.IntegerField(default=777777, max_length=6),
            preserve_default=False,
        ),
    ]
