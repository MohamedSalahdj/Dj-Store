from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from product.models import Brand


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
        """Verify the brand name is correctly set to 'Apple Test'."""
        self.assertEqual(self.brand.name, "Apple Test")

    def test_brand_name_verbose_name(self):
        """Verify the vernose name of brand name is correctly"""
        field_label = self.brand._meta.get_field('name').verbose_name 
        self.assertEqual(field_label, 'Name')

    def test_brand_slug(self):
        """Verify the brand slug starts with a lowercase letter and uses '-' between words."""
        self.assertEqual(self.brand.slug, "apple-test")
    
    def test_brand_image_exists(self):
        """
        Ensure the image is saved in the expected 'brands' directory.
        Verify the image file name contains 'apple'.
        """
        self.assertTrue(self.brand.image.name.startswith("brands/"))
        self.assertIn("apple", self.brand.image.name)


