# Generated by Django 4.2 on 2024-04-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Product',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='4L0C8580', max_length=8, unique=True),
        ),
    ]
