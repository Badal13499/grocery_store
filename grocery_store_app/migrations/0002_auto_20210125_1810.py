# Generated by Django 3.1.5 on 2021-01-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_store_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='item_data',
            name='key',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]