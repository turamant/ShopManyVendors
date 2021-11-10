from django.forms import ModelForm, Select, DecimalField

from apps.product.models import Product, ProductImage


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']
        labels = {'category': 'Категория', 'image': 'Фотография', 'title': 'Наименование',
                  'description': 'Описание',
                  'price': 'Цена'}




class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        labels = {'image': 'Фотография'}