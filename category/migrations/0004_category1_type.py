# Generated by Django 4.2.1 on 2023-05-23 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_type_category1_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category1',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.type'),
            preserve_default=False,
        ),
    ]