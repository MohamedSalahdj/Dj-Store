from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from product.models import Brand


class BrandListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        with open('D:/Courses/Django-fullstack-Course/Django-project/Dj-Store/src/images-tests/apple.png', 'rb') as img:
            cls.image = SimpleUploadedFile(
                name='apple.png',
                content=img.read(),
                content_type='image/png'
            )
            for i in range(35):
                Brand.objects.create(
                    name=f'Samsung-{i}',
                    image=cls.image
                )

    def test_brand_list_status_code(self):
        """Test if the BrandList view returns a 200 status code."""
        response = self.client.get(reverse('product:brand_list'))
        self.assertEqual(response.status_code, 200)

