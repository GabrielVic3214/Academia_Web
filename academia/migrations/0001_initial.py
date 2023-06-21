# Generated by Django 4.2.1 on 2023-06-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('telefone1', models.IntegerField(blank=True, null=True)),
                ('cpf', models.IntegerField()),
                ('cep', models.IntegerField()),
            ],
        ),
    ]
