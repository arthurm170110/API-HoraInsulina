# Generated by Django 4.2 on 2023-04-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refeicao', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refeicao',
            name='horario',
            field=models.TimeField(),
        ),
    ]
