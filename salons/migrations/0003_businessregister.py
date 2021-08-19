# Generated by Django 3.1.4 on 2021-04-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('no_of_workers', models.IntegerField()),
                ('serivice_type', models.CharField(choices=[('home service', 'Home Service'), ('shop', 'Shop'), ('both', 'Both')], max_length=100, null=True)),
                ('address', models.TextField()),
            ],
        ),
    ]