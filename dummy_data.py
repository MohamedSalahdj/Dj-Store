import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand, Product


def seed_brand(number_of_brands):
    fake = Faker()
    Brand_images = ['adidas.logo.png', 'boma.png', 'dell.png', 'Rolex.png', 'gucci.png', 'hp.png', 'lenovo.png', 'nike.jpeg', 'oppo.png', 'polo.png', 'toshiba.png', 'zara.png']
    for _ in range(number_of_brands):
        Brand.objects.create (
            name = fake.name(),
            image = f'brands/{random.choice(Brand_images)}',
        )
    print(f"added {number_of_brands} brands in db")

def seed_products(number_of_products):
    pass


seed_brand(10)