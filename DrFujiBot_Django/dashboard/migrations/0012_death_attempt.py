# Generated by Django 2.2.5 on 2019-10-31 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_bannedphrase'),
    ]

    operations = [
        migrations.AddField(
            model_name='death',
            name='attempt',
            field=models.IntegerField(default=1),
        ),
    ]
