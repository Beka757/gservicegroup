# Generated by Django 4.0.4 on 2022-05-26 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0006_alter_nomenclature_services'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nomenclature',
            options={'ordering': ('id',), 'verbose_name': 'Номенклатура', 'verbose_name_plural': 'Номенклатуры'},
        ),
    ]
