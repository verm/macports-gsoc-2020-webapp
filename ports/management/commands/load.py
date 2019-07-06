import subprocess
import json

from django.core.management.base import BaseCommand, CommandError

from ports.models import Port, Commit

RSYNC_SOURCE = "rsync://rsync.macports.org/macports//trunk/dports/PortIndex_darwin_16_i386/PortIndex.json"
JSON_FILE = "portindex.json"


class Command(BaseCommand):

    help = "Populates the database with Initial data from portindex.json file"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str, default='portindex.json')

    def handle(self, *args, **options):
        try:
            if not Port.objects.count() > 0:
                if options['path'] == "rsync":
                    # Fetch the latest version of portindex2json.json
                    subprocess.call(["rsync", RSYNC_SOURCE, JSON_FILE])

                    # Start loading
                    Port.load(JSON_FILE)

                    # Open the JSON file to find the latest commit
                    with open(JSON_FILE, "r") as file:
                        data = json.load(file)
                    commit = data['info']['commit']

                    # Write this commit to database
                    Commit.objects.create(hash=commit)

                else:
                    Port.load(options['path'])
        except FileNotFoundError:
            raise CommandError('"{}" not found. Make sure "{}" is a valid JSON file and is in the root of the project'.format(
                options['path'], options['path']
            ))
