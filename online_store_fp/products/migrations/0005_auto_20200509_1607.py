# Generated by Django 3.0.5 on 2020-05-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200509_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
