# Generated by Django 4.2 on 2023-05-19 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0037_alter_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='Cupcakaya.item'),
        ),
    ]
