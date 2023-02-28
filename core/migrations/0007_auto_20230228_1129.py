# Generated by Django 3.2 on 2023-02-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230222_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_in',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em:  '),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/service', verbose_name='Foto'),
        ),
    ]
