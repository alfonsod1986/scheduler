# Generated by Django 2.2.24 on 2021-08-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('Enabled', 'ENABLED'), ('Disabled', 'DISABLED')], default='Disabled', max_length=35, verbose_name='Status'),
        ),
    ]