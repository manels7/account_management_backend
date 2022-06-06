from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from accounts.models import Account

class Command(BaseCommand):
	help = 'This command will populate the db with random data to create a demo installation'

	def add_arguments(self, parser):
		parser.add_argument(
			'--force',
			action='store_true',
			dest='force',
			help='Creation of dummy data in DB.',)

	def handle(self, *args, **options):
		self.create_users()
		self.stdout.write("Success: Database populated with dummy entries!\n")

	def create_users(self):
		user1 = User.objects.create(username="armindo", first_name="Armindo", last_name="Freitas")
		user2 = User.objects.create(username="carlos", first_name="Carlos", last_name="Marques")
		user3 = User.objects.create(username="daviJ", first_name="David", last_name="Wallace")
		user4 = User.objects.create(username="fanando", first_name="Manel", last_name="Alberto")
		Account.objects.create(customerID=user2, balance="1000")
		Account.objects.create(customerID=user3, balance="15000000")