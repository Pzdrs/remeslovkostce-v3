from django.core.exceptions import ValidationError
from django.db import models


class ProductCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Product categories'

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MultiGenderLabelModel(models.Model):
    class Meta:
        abstract = True

    label_masculine = models.CharField(max_length=64)
    label_feminine = models.CharField(max_length=64)
    label_neuter = models.CharField(max_length=64)

    def genderize(self, gender: str) -> str:
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
    pass


class ProductSize(models.Model):
    class Unit(models.TextChoices):
        MILLIMETER = 'mm', 'milimetr'
        CENTIMETER = 'cm', 'centimetr'
        METER = 'm', 'metr'

    label = models.ForeignKey(ProductSizeLabel, on_delete=models.SET_NULL, blank=True, null=True)
    sheet_count = models.PositiveIntegerField(blank=True, null=True)

    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField(blank=True, null=True)
    depth = models.PositiveIntegerField()
    unit = models.CharField(max_length=2, choices=Unit.choices, default=Unit.CENTIMETER)

    @property
    def dimensions_display_name(self):
        return f'{self.width}x{self.depth}{f"x{self.height}" if self.height is not None else ""} {self.unit}'

    @property
    def sheet_count_display_name(self):
        return f'{self.sheet_count} listů'

    def get_display_name(self, config: 'SizeDisplayConfiguration', product: 'Product' = None) -> str:
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
            if SizeDisplayConfiguration.DEFAULTS['show_sheet_count'] and self.sheet_count is not None:
                size_attributes.append(self.sheet_count_display_name)
        return ', '.join(size_attributes)

    def __str__(self):
        return f'{self.dimensions_display_name} {f"({self.sheet_count} listů)" if self.sheet_count is not None else ""} ({self.label or "bez popisku"})'


class SizeDisplayConfiguration(models.Model):
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
    hex = models.CharField(max_length=6, default='FFFFFF', blank=True, null=True)

    def __str__(self):
        return f'{super().__str__()} ({f"#{self.hex}" if self.hex is not None else "bez HEX"})'


class Tag(models.Model):
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)

    def get_display_name(self):
        return self.display_name or self.name

    def __str__(self):
        return self.name + f' ({self.display_name})' if self.display_name else ''


class ProductImage(models.Model):
    thumbnail = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')

    def validate_unique(self, exclude=None):
        if self.thumbnail and self.product.images.filter(thumbnail=True).exists():
            raise ValidationError('Produkt může mít pouze jednu náhledovou fotku')
        return super().validate_unique(exclude)

    def __str__(self):
        return f'{self.product.display_name} ({self.image.name})'


class Product(models.Model):
    class Gender(models.TextChoices):
        MASCULINE = 'M', 'mužský'
        FEMININE = 'F', 'ženský'
        NEUTER = 'N', 'střední'

    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    description = models.TextField(blank=True)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, blank=True, null=True)

    tags = models.ManyToManyField(Tag, blank=True)
    show_tags = models.BooleanField(default=True, help_text='Zahrnovat tagy do názvu produktu')

    size = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True, blank=True)
    size_display_configuration = models.ForeignKey(SizeDisplayConfiguration, on_delete=models.SET_NULL, blank=True,
                                                   null=True)

    @property
    def display_name(self):
        color = self.__get_color_display()
        name = self.__get_name_display()
        size = self.__get_size_display()
        tags = self.__get_tags_display()
        return f'{color + " " if color else ""}{name}{f", {size}" if size else ""}{f", {tags}" if tags else ""}'

    @property
    def thumbnail(self) -> ProductImage:
        return self.images.filter(thumbnail=True).first()

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
