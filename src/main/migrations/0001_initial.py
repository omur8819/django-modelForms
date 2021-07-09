# Generated by Django 3.2.5 on 2021-07-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('age', models.CharField(max_length=3)),
            ],
        ),
    ]
