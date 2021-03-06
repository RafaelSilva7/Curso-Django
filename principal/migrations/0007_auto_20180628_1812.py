# Generated by Django 2.0.6 on 2018-06-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_entrada_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagem',
            field=models.TextField(blank=True, null=True, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='texto',
            field=models.TextField(blank=True, null=True, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título'),
        ),
    ]
