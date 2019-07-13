from django.core.management.base import BaseCommand, CommandError

from ports.models import Port, LastPortIndexUpdate
from parsing_scripts import rsync_operations


class Command(BaseCommand):

    help = "Populates the database with Initial data after fetching portindex.json from rsync"

    def handle(self, *args, **options):
        if not Port.objects.count() > 0:
            # Fetch from rsync
            rsync_operations.sync()

            # Open the file
            data = rsync_operations.open_file()

            # Start populating
            Port.load(data['ports'])

            # Write the commit hash into database
            if LastPortIndexUpdate.objects.count() > 0:
                last_commit = LastPortIndexUpdate.objects.all().first()
                last_commit.git_commit_hash = data['info']['commit']
                last_commit.save()
            else:
                LastPortIndexUpdate.objects.create(git_commit_hash=data['info']['commit'])

            print("Successfully loaded the database.")
