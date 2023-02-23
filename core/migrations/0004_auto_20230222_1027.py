# Generated by Django 3.2 on 2023-02-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_cnpj_supplier_cnpj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user',
        ),
        migrations.AddField(
            model_name='client',
            name='cep',
            field=models.CharField(default='', max_length=9, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(default='', max_length=50, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='client',
            name='district',
            field=models.CharField(default='', max_length=50, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='client',
            name='fullname',
            field=models.CharField(default='', max_length=100, verbose_name='Nome Completo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default='', max_length=11, verbose_name='telefone'),
        ),
        migrations.AddField(
            model_name='client',
            name='property_number',
            field=models.CharField(default=0, max_length=5, verbose_name='Número'),
        ),
        migrations.AddField(
            model_name='client',
            name='uf',
            field=models.CharField(default='', max_length=2, verbose_name='UF'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='fantasy_name',
            field=models.CharField(default='', max_length=100, verbose_name='Razão Social'),
            preserve_default=False,
        ),
    ]