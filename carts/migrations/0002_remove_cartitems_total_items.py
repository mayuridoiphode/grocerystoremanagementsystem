# Generated by Django 2.2.7 on 2023-09-08 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='total_items',
        ),
    ]