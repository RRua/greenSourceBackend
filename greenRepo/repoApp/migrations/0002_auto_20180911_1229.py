# Generated by Django 2.1 on 2018-09-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='androidproject',
            name='project_desc',
            field=models.CharField(default='', max_length=64, null=True),
        ),
    ]
