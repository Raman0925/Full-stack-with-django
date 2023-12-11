# seeds.py

from django_seed import Seed
from seedapp.models import MyModel

seeder = Seed.seeder()

# Define the model and the number of instances to create
seeder.add_entity(MyModel, 10, {
    'name': lambda x: seeder.faker.name(),
    'first_name': lambda x: seeder.faker.first_name(),
    'roll': lambda x: seeder.faker.random_number(),
})

# Execute the seeding process
inserted_pks = seeder.execute()
