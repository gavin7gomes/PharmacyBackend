# Generated by Django 3.2.12 on 2022-03-04 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_orderitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderItems',
        ),
    ]
