# Generated by Django 3.0.5 on 2020-05-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_postadd_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y%m%d %H%m'),
        ),
    ]
