from rest_framework import serializers

from remeslovkostce.models import Product, ProductCategory, ProductImage, ProductSize, ProductColor


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ('sheet_count', 'width', 'height', 'depth', 'unit')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'display_name', 'description', 'tags', 'size', 'color', 'thumbnail')

    display_name = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    size = ProductSizeSerializer()
    color = serializers.SerializerMethodField()

    def get_display_name(self, obj: Product):
        return obj.display_name

    def get_thumbnail(self, obj: Product):
        return obj.thumbnail.image.name if obj.thumbnail else None

    def get_color(self, obj: Product):
        return {
            'label': obj.color.genderize('F'),
            'hex': obj.color.hex
        } if obj.color else None


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
