# Generated by Django 4.2.1 on 2023-06-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=500)),
                ('link', models.CharField(blank=True, max_length=500)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
