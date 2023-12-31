# Generated by Django 4.2.7 on 2023-11-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findata', '0002_remove_depositproducts_user_pk_and_more'),
        ('accounts', '0002_alter_user_money_alter_user_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='financial_products',
        ),
        migrations.AddField(
            model_name='user',
            name='financial_products_deposit',
            field=models.ManyToManyField(to='findata.depositproducts'),
        ),
        migrations.AddField(
            model_name='user',
            name='financial_products_saving',
            field=models.ManyToManyField(to='findata.savingsproducts'),
        ),
    ]
