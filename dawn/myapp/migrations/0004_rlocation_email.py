# Generated by Django 2.1.2 on 2018-11-11 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181111_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='rlocation',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
