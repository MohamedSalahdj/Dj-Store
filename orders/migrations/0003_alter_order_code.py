# Generated by Django 4.2 on 2024-04-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='J7H0NJ7H', max_length=8, unique=True),
        ),
    ]
