# Generated by Django 2.0.7 on 2018-08-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0011_auto_20180805_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='Activewear', max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(default='Female', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(default='S M L', max_length=60),
        ),
    ]