# Generated by Django 2.1.7 on 2020-01-31 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200130_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
    ]
