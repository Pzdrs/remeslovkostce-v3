# Generated by Django 4.2.3 on 2023-07-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remeslovkostce', '0019_alter_tag_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='order_weight',
            field=models.IntegerField(default=0),
        ),
    ]