# Generated by Django 2.2.24 on 2021-08-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20210809_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(choices=[('Enabled', 'ENABLED'), ('Disabled', 'DISABLED')], default='Enabled', max_length=35, verbose_name='Status'),
        ),
    ]
