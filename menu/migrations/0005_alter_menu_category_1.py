# Generated by Django 4.2.1 on 2023-07-27 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_category1_type'),
        ('menu', '0004_menu_category_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menues', to='category.category1'),
        ),
    ]
