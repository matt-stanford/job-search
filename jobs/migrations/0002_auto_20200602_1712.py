# Generated by Django 3.0.5 on 2020-06-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobId',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
