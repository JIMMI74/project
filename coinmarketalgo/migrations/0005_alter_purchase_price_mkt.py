# Generated by Django 4.0.2 on 2022-02-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinmarketalgo', '0004_alter_purchase_price_mkt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='price_mkt',
            field=models.FloatField(default=0.897581),
        ),
    ]
