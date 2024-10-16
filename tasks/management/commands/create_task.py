from faker import Faker
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task
import random


class Command(BaseCommand):
    help = "Create random task"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.root_user = User.objects.get(username="root")
        self.fake = Faker()

    def handle(self, *args, **options):
        for _ in range(0, 10):
            Task.objects.create(
                title=self.fake.word(),
                description=self.fake.paragraph(nb_sentences=1),
                done=random.choice([True, False]),
                creator=self.root_user,
            )
