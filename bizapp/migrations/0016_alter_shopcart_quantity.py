# Generated by Django 3.2.7 on 2021-09-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizapp', '0015_shopcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
