# Generated by Django 4.2 on 2023-05-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0027_amount_price_flavours_price_alter_coverage_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('comment', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
