# Generated by Django 2.1 on 2018-09-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repoApp', '0002_auto_20180911_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='androidproject',
            name='project_desc',
            field=models.CharField(default='', max_length=64),
        ),
    ]
