# Generated by Django 4.2.3 on 2023-07-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remeslovkostce', '0006_tag_product_show_tags_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='display_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]