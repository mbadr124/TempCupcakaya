# Generated by Django 4.2 on 2023-05-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0036_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='Cupcakaya.orderitem'),
        ),
    ]
