# Generated by Django 4.2 on 2024-04-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='K8F2FDGA', max_length=8, unique=True),
        ),
    ]
