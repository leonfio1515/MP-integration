# Generated by Django 4.2.6 on 2023-10-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0002_cliente_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='unit_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]