# Generated by Django 4.2.7 on 2023-11-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]