# Generated by Django 4.2.17 on 2025-03-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_order_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_shipped',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
