# Generated by Django 5.0.4 on 2024-05-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inserirfalta',
            name='ano_aluno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inserirfalta',
            name='dias_afastado',
            field=models.IntegerField(),
        ),
    ]