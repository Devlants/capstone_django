# Generated by Django 4.2.1 on 2023-05-23 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_menu_category_3'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category3',
        ),
    ]
