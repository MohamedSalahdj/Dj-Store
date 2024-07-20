# Generated by Django 4.2 on 2024-04-30 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_cartdetail_quantity_alter_order_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cupon',
            new_name='Coupon',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cupon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cupon',
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_coupon', to='orders.coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_coupon', to='orders.coupon'),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='DNNJA15K', max_length=8, unique=True),
        ),
    ]