# Generated by Django 2.1.5 on 2022-05-21 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_auto_20190105_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'Historia', 'verbose_name_plural': 'Historia'},
        ),
        migrations.AlterModelOptions(
            name='chef',
            options={'verbose_name': 'staff', 'verbose_name_plural': 'staff'},
        ),
        migrations.AlterModelOptions(
            name='why_choose_us',
            options={'verbose_name': 'Virtud', 'verbose_name_plural': 'Virtudes'},
        ),
    ]
