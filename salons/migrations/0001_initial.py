# Generated by Django 3.1.4 on 2021-04-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('header', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, choices=[('johar town', 'johar town'), ('pia Society', 'pia Society'), ('dha', 'dha'), ('bahria town', 'bahria town')], max_length=50, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='SalomImages/')),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='SalonImages/')),
                ('center_image', models.ImageField(blank=True, null=True, upload_to='SalonImages/')),
            ],
        ),
    ]
