# Generated by Django 4.2.3 on 2023-07-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remeslovkostce', '0003_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
