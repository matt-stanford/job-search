# Generated by Django 3.0.5 on 2020-06-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]