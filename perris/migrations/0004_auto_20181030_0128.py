# Generated by Django 2.1.2 on 2018-10-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perris', '0003_auto_20181028_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro',
            name='persona',
        ),
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.CharField(max_length=10),
        ),
    ]
