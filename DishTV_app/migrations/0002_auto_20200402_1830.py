# Generated by Django 3.0.4 on 2020-04-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DishTV_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]