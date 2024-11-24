from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from product.models import Product, Brand


class ProductTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        with open(r'D:/Courses/Django-fullstack-Course/Django-project/Dj-Store/src/images-tests/samsung.png', 'rb') as img:
            cls.brand_image = SimpleUploadedFile(
                name='samsung.png',
                content=img.read(),
                content_type='image/png'
            )

        with open(r'D:/Courses/Django-fullstack-Course/Django-project/Dj-Store/src/images-tests/iphone16.jpg', 'rb') as img:
            cls.product_image = SimpleUploadedFile(
                name='iphone16.jpg',
                content=img.read(),
                content_type='image/jpg'
            )
        
        cls.brand = Brand.objects.create(
            name='Samsung',
            image=cls.brand_image
        )

        cls.product = Product.objects.create(
            name='iPhone 16',
            image=cls.product_image,
            price=79299,
            quantity=5,
            flag='New',
            description=r'The iPhone 16 features a powerful A18 Bionic chip with up to 30% faster CPU performance and 40% faster GPU capabilities compared to previous models. It boasts an extended battery life, with up to 27 hours of video playback on the iPhone 16 Plus. The design incorporates aerospace-grade aluminum and color-infused glass for enhanced durability, alongside an improved Ceramic Shield that is twice as tough as any smartphone glass.',
            sku='IP16PRO1234',
            subtittle='Apple iPhone 16 Pro Max (256 GB) - Desert Titanium',
            brand=cls.brand
        )

    def test_product_name(self):
        """Test the product name is correctly set to 'iPhone 16'."""
        self.assertEqual(self.product.name, "iPhone 16")

    def test_product_name_verbose_name(self):
        """Test the verbose name of product name is correctly"""
        field_label = self.product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')

    def test_product_max_length(self):
        """Test the product max_length of the 'name' field is 125."""
        max_length = self.product._meta.get_field('name').max_length
        self.assertTrue(max_length==125)