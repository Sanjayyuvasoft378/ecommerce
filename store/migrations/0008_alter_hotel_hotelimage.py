# Generated by Django 3.2.15 on 2022-09-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_hotel_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotelImage',
            field=models.ImageField(upload_to='Media/'),
        ),
    ]
