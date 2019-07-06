import subprocess
import json

from django.core.management.base import BaseCommand, CommandError

from parsing_scripts import git_update
from ports.models import Port

RSYNC_SOURCE = "rsync://rsync.macports.org/macports//trunk/dports/PortIndex_darwin_16_i386/PortIndex.json"
JSON_FILE = "portindex.json"


class Command(BaseCommand):
    help = "Populates the database with Initial data from portindex.json file"

    def add_arguments(self, parser):
        parser.add_argument('new',
                            nargs='?',
                            default=False,
                            help="Define a commit till which the update should be processed")
        parser.add_argument('old',
                            nargs='?',
                            default=False,
                            help="Not recommended. Helps you provide a commit from which update should start")

    def handle(self, *args, **options):
        if options['new'] is False:
            # Fetch the latest version of portindex2json.json
            subprocess.call(["rsync", RSYNC_SOURCE, JSON_FILE])

            # Open the JSON file to find the latest commit
            with open(JSON_FILE, "r") as file:
                data = json.load(file)

            # set new hash to the hash obtained from json file
            options['new'] = data['info']['commit']

        ports_to_be_updated = git_update.get_list_of_changed_ports(options['new'], options['old'])
        Port.update(ports_to_be_updated)


