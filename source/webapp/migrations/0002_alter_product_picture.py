# Generated by Django 3.2.15 on 2022-08-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='images/photo-1.jpg', null=True, upload_to='images/', verbose_name='Картинка'),
        ),
    ]
