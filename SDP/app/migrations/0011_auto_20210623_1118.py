# Generated by Django 3.1.6 on 2021-06-23 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210619_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='symptom6',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom7',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='hospital',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
    ]
