# Generated by Django 4.1.6 on 2023-02-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlmacenApp', '0012_remove_movimientos_id_alter_movimientos_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
