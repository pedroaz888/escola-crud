# Generated by Django 4.1.3 on 2022-11-14 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_aluno_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='foto',
        ),
    ]
