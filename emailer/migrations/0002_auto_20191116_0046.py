# Generated by Django 2.2.3 on 2019-11-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='message_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
