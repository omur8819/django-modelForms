# Generated by Django 3.2.5 on 2021-07-09 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('id',)},
        ),
    ]
