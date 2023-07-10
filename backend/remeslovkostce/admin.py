from django.contrib import admin

from remeslovkostce.models import ProductCategory, Product, ProductColor, ProductSizeLabel, ProductSize, Tag


# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'display_name', 'gender', 'color')

    @admin.display()
    def display_name(self, obj):
        return obj.display_name


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductSizeLabel)
class ProductSizeLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
