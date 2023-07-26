from django.core.exceptions import ValidationError
from django.db import models


class Tag(models.Model):
    """
    A Tag is a label that can be attached to a product, product color, product size,
    product category or variant group.
    """

    class Type(models.TextChoices):
        """
        The type of tag determines where it can be attached.
        """
        CATEGORY = 'category', 'Tag kategorie'
        PRODUCT = 'product', 'Tag produktu'
        PRODUCT_COLOR = 'product_color', 'Tag barvy produktu'
        PRODUCT_SIZE = 'product_size', 'Tag velikosti produktu'
        VARIANT_GROUP = 'variant_group', 'Tag skupiny variant'

    name = models.CharField(max_length=64)
    type = models.CharField(max_length=16, choices=Type.choices)
    display_name = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)

    def get_display_name(self):
        """
        :return: The display name of the tag, if it is set. Otherwise, the name is returned.
        """
        return self.display_name or self.name

    def __str__(self):
        return self.name + (f'({self.display_name})' if self.display_name else '')


class ProductCategory(models.Model):
    """
    A category of products. A product can only belong to one category.
    """

    class Meta:
        verbose_name_plural = 'Product categories'
        ordering = ('order_weight',)

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, limit_choices_to={'type': Tag.Type.CATEGORY}, blank=True)
    order_weight = models.IntegerField(default=0)

    @property
    def product_count(self):
        """
        :return: The number of products assigned to this category.
        """
        return self.product_set.all().count()

    def __str__(self):
        return self.name


class MultiGenderLabelModel(models.Model):
    """
    This model represents an entity whose name needs to be gendered.
    """

    class Meta:
        abstract = True

    label_masculine = models.CharField(max_length=64)
    label_feminine = models.CharField(max_length=64)
    label_neuter = models.CharField(max_length=64)

    def genderize(self, gender: str) -> str:
        """
        :return: The the correct label based on the passed in gender.
        """
        match gender:
            case Product.Gender.MASCULINE:
                return self.label_masculine
            case Product.Gender.FEMININE:
                return self.label_feminine
            case Product.Gender.NEUTER:
                return self.label_neuter
            case _:
                return f'{self.label_masculine} / {self.label_feminine} / {self.label_neuter}'

    def __str__(self):
        return f'{self.label_masculine} / {self.label_feminine} / {self.label_neuter}'


class ProductSizeLabel(MultiGenderLabelModel):
    """
    Intermediary model for product size labels.
    """


class ProductSize(models.Model):
    """
    This model holds all the information about a product size and dimensions.
    """

    class Unit(models.TextChoices):
        """
        Metric units of measurement for a given instance.
        """
        MILLIMETER = 'mm', 'milimetr'
        CENTIMETER = 'cm', 'centimetr'
        METER = 'm', 'metr'

    label = models.ForeignKey(ProductSizeLabel, on_delete=models.SET_NULL, blank=True, null=True)
    sheet_count = models.PositiveIntegerField(blank=True, null=True)

    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField(blank=True, null=True)
    depth = models.PositiveIntegerField()
    unit = models.CharField(max_length=2, choices=Unit.choices, default=Unit.CENTIMETER)

    tags = models.ManyToManyField(Tag, limit_choices_to={'type': Tag.Type.PRODUCT_SIZE}, blank=True)

    @property
    def dimensions_display_name(self):
        """
        :return: The dimensions of the product size in the
        format "width x depth x height unit".
        """
        return f'' \
               f'{self.width}x{self.depth}{f"x{self.height}" if self.height is not None else ""} ' \
               f'{self.unit}'

    @property
    def sheet_count_display_name(self):
        """
        :return: The number of sheets in the product
        size in the format "sheet_count listů".
        """
        return f'{self.sheet_count} listů'

    def get_display_name(
            self,
            config: 'SizeDisplayConfiguration',
            product: 'Product' = None
    ) -> str:
        """
        :return: The display name of the product size. If a configuration
        is passed in, the display name is generated
        """
        size_attributes = []

        if config:
            if config.show_label and self.label:
                size_attributes.append(self.label.genderize(product.gender if product else None))
            if config.show_dimensions:
                size_attributes.append(self.dimensions_display_name)
            if config.show_sheet_count and self.sheet_count is not None:
                size_attributes.append(self.sheet_count_display_name)
        else:
            if SizeDisplayConfiguration.DEFAULTS['show_label'] and self.label:
                size_attributes.append(self.label.genderize(product.gender if product else None))
            if SizeDisplayConfiguration.DEFAULTS['show_dimensions']:
                size_attributes.append(self.dimensions_display_name)
            if SizeDisplayConfiguration.DEFAULTS['show_sheet_count'] \
                    and self.sheet_count is not None:
                size_attributes.append(self.sheet_count_display_name)
        return ', '.join(size_attributes)

    def __str__(self):
        return f'{self.dimensions_display_name} ' \
               f'{f"({self.sheet_count} listů)" if self.sheet_count is not None else ""} ' \
               f'({self.label or "bez popisku"})'


class SizeDisplayConfiguration(models.Model):
    """
    This model holds the configuration for how a product size should
    be displayed in the product name.
    """
    DEFAULTS = {
        'show_label': True,
        'show_sheet_count': True,
        'show_dimensions': False
    }
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    show_label = models.BooleanField(
        default=DEFAULTS['show_label'],
        help_text='Zahrnovat popisek velikosti do názvu produktu'
    )
    show_sheet_count = models.BooleanField(
        default=DEFAULTS['show_sheet_count'],
        help_text='Zahrnovat počet listů do názvu produktu'
    )
    show_dimensions = models.BooleanField(
        default=DEFAULTS['show_dimensions'],
        help_text='Zahrnovat rozměry do názvu produktu'
    )

    def __str__(self):
        return self.size.get_display_name(self)


class ProductColor(MultiGenderLabelModel):
    """
    This model holds all the information about a product color.
    """
    hex = models.CharField(max_length=6, default='FFFFFF', blank=True, null=True)
    tags = models.ManyToManyField(
        Tag, limit_choices_to={'type': Tag.Type.PRODUCT_COLOR}, blank=True
    )

    def __str__(self):
        return f'{super().__str__()} ({f"#{self.hex}" if self.hex is not None else "bez HEX"})'


class ProductImage(models.Model):
    """
    This model holds all the information about a product image.
    """
    thumbnail = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')

    def validate_unique(self, exclude=None):
        if self.thumbnail and self.product.images.filter(thumbnail=True).exists():
            raise ValidationError('Produkt může mít pouze jednu náhledovou fotku')
        return super().validate_unique(exclude)

    def __str__(self):
        return f'{self.product.display_name} ({self.image.name})'


class VariantGroup(models.Model):
    """
    A variant group is a collection of products that are similar,
    but differ in some way, e.g. color.
    """
    name = models.CharField(max_length=64)
    tags = models.ManyToManyField(
        Tag, limit_choices_to={'type': Tag.Type.VARIANT_GROUP}, blank=True
    )

    def __str__(self):
        return self.name

    def get_product_ids(self, product: 'Product' = None):
        """
        :return: A list of product IDs that belong to this variant group,
        excluding the passed in product.
        """
        products = self.product_set
        if product:
            products = products.exclude(pk=product.pk)
        return list(products.values_list('pk', flat=True))

    def get_product_count(self):
        """
        :return: The number of products that belong to this variant group.
        """
        return self.product_set.count()


class Product(models.Model):
    """
    This model holds all the information about a product.
    """

    class Gender(models.TextChoices):
        """
        Defines what gender should be used in the display name generation process.
        """
        MASCULINE = 'M', 'mužský'
        FEMININE = 'F', 'ženský'
        NEUTER = 'N', 'střední'

    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    description = models.TextField(blank=True)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, blank=True, null=True)

    tags = models.ManyToManyField(Tag, limit_choices_to={'type': Tag.Type.PRODUCT}, blank=True)
    show_tags = models.BooleanField(default=True, help_text='Zahrnovat tagy do názvu produktu')

    size = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True, blank=True)
    size_display_configuration = models.ForeignKey(
        SizeDisplayConfiguration, on_delete=models.SET_NULL, blank=True, null=True
    )

    variant_group = models.ForeignKey(
        VariantGroup, on_delete=models.SET_NULL, blank=True, null=True
    )

    @property
    def display_name(self) -> str:
        """
        :return: The display name of the product.
        """
        color = self.__get_color_display()
        name = self.__get_name_display()
        size = self.__get_size_display()
        tags = self.__get_tags_display()
        return f'{color + " " if color else ""}' \
               f'{name}' \
               f'{f", {size}" if size else ""}' \
               f'{f", {tags}" if tags else ""}'

    @property
    def thumbnail(self) -> ProductImage:
        """
        :return: The thumbnail image of the product.
        """
        return self.images.filter(thumbnail=True).first()

    def get_variants(self):
        """
        :return: A list of product IDs that belong to this variant group, excluding
        the passed in product.
        """
        if not self.variant_group:
            return []
        return self.variant_group.get_product_ids(self)

    def __get_tags_display(self):
        if not self.show_tags:
            return ''
        return ', '.join([tag.get_display_name() for tag in self.tags.all()])

    def __get_color_display(self):
        return self.color.genderize(self.gender) if self.color else None

    def __get_name_display(self):
        name_display = self.name

        # If no color is set, capitalize the first letter of the name
        if not self.color:
            name_display = name_display.capitalize()

        return name_display

    def __get_size_display(self):
        return self.size.get_display_name(self.size_display_configuration, self)

    def __str__(self):
        return self.display_name
