# Generated by Django 4.2 on 2023-05-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_view', '0002_alter_product_options_alter_product_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(default='', max_length=100, null=True)),
                ('order_location', models.CharField(default='', max_length=200, null=True)),
                ('order_data', models.TextField()),
            ],
        ),
    ]
