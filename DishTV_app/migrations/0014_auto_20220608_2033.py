# Generated by Django 3.2.13 on 2022-06-08 15:03

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DishTV_app', '0013_auto_20200513_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='added_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='contact_us',
            old_name='added_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='processed_on',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='added_on',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='update_on',
        ),
        migrations.RemoveField(
            model_name='register_table',
            name='added_on',
        ),
        migrations.RemoveField(
            model_name='register_table',
            name='update_on',
        ),
        migrations.AddField(
            model_name='add_product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact_us',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register_table',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
