# Generated by Django 3.1.4 on 2021-07-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0025_service_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='service/'),
        ),
    ]