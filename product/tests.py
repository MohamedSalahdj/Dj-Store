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
            cls.brand = Brand.objects.create(
                name='Apple Test',
                image=cls.image
            )

    def test_brand_name(self):
        self.assertEqual(self.brand.name, "Apple Test")

    def test_brand_slug(self):
        self.assertEqual(self.brand.slug, "apple-test")
    
    def test_brand_image_exists(self):
        self.assertTrue(self.brand.image.name.startswith("brands/"))
        self.assertIn("apple", self.brand.image.name)

