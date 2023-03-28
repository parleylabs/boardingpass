from django.core.management.base import BaseCommand
from api.services.chirpstack_internal import chirpstack_login


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Running Test Code")



