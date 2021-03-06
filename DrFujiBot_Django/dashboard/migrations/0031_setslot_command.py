# Generated by Django 2.2.8 on 2020-11-21 09:22

from django.db import migrations
from dashboard.models import MODERATOR_ONLY

def create_setslot_command(apps, schema_editor):
    Command = apps.get_model('dashboard', 'Command')
    cmd = Command(command="!setslot", permissions=MODERATOR_ONLY, is_built_in=True, cooldown=False, output=None)
    cmd.save()

def create_sprites_setting(apps, schema_editor):
    Setting = apps.get_model('dashboard', 'Setting')

    sprites_folder_setting = Setting(key='Sprites Folder', value='')

    sprites_folder_setting.save()

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_increase_setting_value_size'),
    ]

    operations = [
        migrations.RunPython(create_setslot_command),
        migrations.RunPython(create_sprites_setting),

    ]
