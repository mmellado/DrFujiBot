# Generated by Django 2.2.5 on 2019-10-15 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_default_run'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', models.CharField(max_length=1000)),
                ('quotee', models.CharField(max_length=200)),
            ],
        ),
    ]