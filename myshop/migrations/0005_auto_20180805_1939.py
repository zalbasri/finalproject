# Generated by Django 2.0.7 on 2018-08-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_auto_20180805_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(default='Male', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(default='S M L', max_length=60),
        ),
    ]
