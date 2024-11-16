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

    def test_brand_list_template(self):
        """Test if the correct template is used for BrandList view."""
        response = self.client.get(reverse('product:brand_list'))
        self.assertTemplateUsed(response, 'product/brand_list.html')

    def test_brand_list_pagination(self):
        """Test if pagination returns correct number of brands per page."""
        response = self.client.get(reverse('product:brand_list'))
        self.assertIn('is_paginated', response.context)
        self.assertEqual(len(response.context['brand_list']), 20)
    
    def test_brand_list_pagination_second_page(self):
        """Test if second page of pagination returns the remaining 15 brands."""
        response = self.client.get(reverse('product:brand_list') + '?page=2')
        self.assertEqual(len(response.context['brand_list']), 15)
    
    def test_brand_list_queryset_annotation(self):
        """Test if the 'product_count' annotation is included in the queryset."""
        response = self.client.get(reverse('product:brand_list'))
        brand_list = response.context['brand_list']
        self.assertTrue(hasattr(brand_list[0], 'product_count'))
    
    def test_brand_list_queryset_annotation_count(self):
        """Test if the 'product_count' equal zero annotation is included in the queryset."""
        response = self.client.get(reverse('product:brand_list'))
        brand_list = response.context['brand_list']
        self.assertEqual(brand_list[0].product_count, 0)
    
    