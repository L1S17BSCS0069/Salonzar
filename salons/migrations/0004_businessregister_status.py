# Generated by Django 3.1.4 on 2021-04-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0003_businessregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessregister',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], max_length=100, null=True),
        ),
    ]
