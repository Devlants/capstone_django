# Generated by Django 4.2.1 on 2023-07-29 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 7, 29, 15, 7, 55, 634451, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]