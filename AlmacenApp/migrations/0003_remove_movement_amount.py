# Generated by Django 4.1.7 on 2023-02-19 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlmacenApp', '0002_movement_price_alter_movement_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movement',
            name='amount',
        ),
    ]