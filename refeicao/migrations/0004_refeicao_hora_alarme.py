# Generated by Django 4.2 on 2023-04-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refeicao', '0003_alter_refeicao_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='refeicao',
            name='hora_alarme',
            field=models.TimeField(null=True),
        ),
    ]
