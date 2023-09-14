import os, django
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
    fake = Faker()
    product_images = ['p-01.jpeg', 'p-02.jpeg', 'p-03.jpeg', 'p-04.jpeg', 'p-05.jpeg', 'p-05.png', 'p-06.jpeg', 'p-07.jpeg', 'p-08.jpeg', 'p-10.jpeg', 'p-11.jpeg', 'p-12.jpeg']
    product_tages = ['Mobile', 'Sport', 'Laptop', 'Computer', 'Clothes', 'Smartwatch', 'wristwatch', 'shirt', 'Nike', 'Gucci', 'HP', 'DELL', 'OPPO', 'POLO', 'ROLEX', 'ZARA', 'Boma']
    flags = ['Sale', 'New', 'Feature']
    
    for _ in range(number_of_products):
        Product.objects.create (
            name = fake.name(), 
            image = f'products/{product_images[random.randint(0, 11)]}',
            price = round(random.uniform(30, 30000), 2),
            quantity = random.randint(0, 15),
            flag = random.choice(flags),
            description = fake.text(max_nb_chars=3000),
            sku = random.randint(100, 102054),
            subtittle = fake.text(max_nb_chars=270),
            brand = Brand.objects.get(id=random.randint(1, 100)),
        )
    print(f"added {number_of_products} Products in db")


# seed_brand(88)
# seed_products(15)

