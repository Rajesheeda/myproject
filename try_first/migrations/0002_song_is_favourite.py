# Generated by Django 2.1.7 on 2019-03-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try_first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
