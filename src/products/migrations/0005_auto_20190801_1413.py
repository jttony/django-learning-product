# Generated by Django 2.2.3 on 2019-08-01 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190801_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Title',
            new_name='title',
        ),
    ]
