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

    def get_display_name(self, product: 'Product'):
        if self.label is None:
            size_attributes = []
            if product.show_dimensions:
                size_attributes.append(self.dimensions_display_name)
            if product.show_sheet_count:
                size_attributes.append(self.sheet_count_display_name)

            return ', '.join(size_attributes)
        return self.label.genderize(product.gender)

    def __str__(self):
        return f'{self.dimensions_display_name} {f"({self.sheet_count} listů)" if self.sheet_count is not None else ""} ({self.label or "bez popisku"})'


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
        return self.name


class Product(models.Model):
    class Gender(models.TextChoices):
        MASCULINE = 'M', 'mužský'
        FEMININE = 'F', 'ženský'
        NEUTER = 'N', 'střední'

    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    description = models.TextField(blank=True)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, null=True)

    tags = models.ManyToManyField(Tag, blank=True)
    show_tags = models.BooleanField(default=True)

    size = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True)
    show_sheet_count = models.BooleanField(default=True)
    show_dimensions = models.BooleanField(default=True)

    @property
    def display_name(self):
        return f'{self.__get_color_display()} {self.__get_name_display()}, {self.__get_size_display()}{self.__get_tags_display()}'

    def __get_tags_display(self):
        if not self.show_tags:
            return ''
        tags = self.tags.all()
        return (', ' if tags else '') + ', '.join([tag.get_display_name() for tag in tags])

    def __get_color_display(self):
        return self.color.genderize(self.gender).capitalize()

    def __get_name_display(self):
        return self.name.lower()

    def __get_size_display(self):
        return self.size.get_display_name(self).lower()

    def __str__(self):
        return self.display_name
