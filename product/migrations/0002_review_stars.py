# Generated by Django 5.2 on 2025-04-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]
