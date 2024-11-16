from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Brand, Product


class BrandTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        with open(r'D:/Courses/Django-fullstack-Course/Django-project/Dj-Store/src/images-tests/apple.png', 'rb') as img:
            cls.image = SimpleUploadedFile(
                name='apple.png', 
                content=img.read(),
                content_type='image/png')
            Brand.objects.create(
                name='Apple',
                image=cls.image
            )

    def test_brand_name(self):
        brand = Brand.objects.get(id=1)
        self.assertEqual(brand.name, "Apple")