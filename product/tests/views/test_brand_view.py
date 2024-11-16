from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
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

