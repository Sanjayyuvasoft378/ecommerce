# Generated by Django 3.2.15 on 2022-09-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discountName', models.CharField(max_length=20)),
                ('discountValue', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Discount',
            },
        ),
    ]