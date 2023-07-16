from rest_framework import serializers

from remeslovkostce.models import Product, ProductCategory, ProductImage, ProductSize, ProductColor


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'thumbnail', 'image')


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ('sheet_count', 'width', 'height', 'depth', 'unit', 'dimensions_display_name')

    dimensions_display_name = serializers.SerializerMethodField()

    def get_dimensions_display_name(self, obj: ProductSize):
        return obj.dimensions_display_name


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'category', 'display_name', 'description', 'tags', 'size', 'color', 'thumbnail'
        )

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


class ProductDetailSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'category', 'display_name', 'description', 'tags', 'size', 'color', 'thumbnail', 'images',
            'variants'
        )

    images = ProductImageSerializer(many=True)
    variants = serializers.SerializerMethodField()

    def get_variants(self, obj: Product):
        return {
            'name': obj.variant_group.name,
            'products': obj.get_variants()
        } if obj.variant_group else None


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    products = serializers.SerializerMethodField()

    def get_products(self, obj: ProductCategory):
        return obj.product_count
