# Generated by Django 4.2.3 on 2023-07-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remeslovkostce', '0017_tag_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcolor',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 'product_color'}, to='remeslovkostce.tag'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 'product_size'}, to='remeslovkostce.tag'),
        ),
        migrations.AddField(
            model_name='variantgroup',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 'variant_group'}, to='remeslovkostce.tag'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 'product'}, to='remeslovkostce.tag'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 'category'}, to='remeslovkostce.tag'),
        ),
    ]
