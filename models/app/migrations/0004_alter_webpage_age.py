# Generated by Django 5.1.5 on 2025-03-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_webpage_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='age',
            field=models.IntegerField(default='22'),
        ),
    ]
