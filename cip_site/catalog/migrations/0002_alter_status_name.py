# Generated by Django 4.1.4 on 2023-02-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(default='In-Process', help_text='Enter a status for CIP', max_length=20, unique=True),
        ),
    ]