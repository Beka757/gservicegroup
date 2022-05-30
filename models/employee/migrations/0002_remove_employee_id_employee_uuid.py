# Generated by Django 4.0.4 on 2022-05-28 09:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100000, primary_key=True, serialize=False),
        ),
    ]