# Generated by Django 4.1.1 on 2022-12-20 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_of_activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_of_event']},
        ),
    ]