# Generated by Django 2.2.5 on 2019-09-30 09:57

from django.db import migrations
from dashboard.models import MODERATOR_ONLY

lookup_commands = ['!pokemon',
                   '!move',
                   '!ability',
                   '!learnset',
                   '!tmset',
                   '!faster',
                   '!item',
                   '!evolve',
                   '!weak',
                   '!resist',
                   '!type',
                   '!catchrate',
                   '!expcurve',
                   '!offense',
                   '!offence',
                   '!defense',
                   '!defence',
                   '!whatis',
                   '!does',
                   '!grassknot',
                   '!lowkick',
                   '!baseexp',
                   '!evyield',
                   '!nature',
                  ]

def create_lookup_commands(apps, schema_editor):
    Command = apps.get_model('dashboard', 'Command')

    commands = []
    for lookup_command in lookup_commands:
        cmd = Command(command=lookup_command, permissions=MODERATOR_ONLY, invocation_count=0, is_built_in=True, cooldown=False, output=None)
        commands.append(cmd)

    Command.objects.bulk_create(commands)

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_lookup_commands),
    ]
