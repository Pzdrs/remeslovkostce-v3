# Generated by Django 4.2.3 on 2023-07-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remeslovkostce', '0007_tag_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prefer_label',
            field=models.BooleanField(default=True, help_text='Pokud je zaškrtnuto a je nastaven popisek velikosti, v názvu se zobrazí popisek namísto rozměrů a počtu listů. V opačném případě se zobrazí všechny tři atributy.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='show_dimensions',
            field=models.BooleanField(default=True, help_text='Zahrnovat rozměry do názvu produktu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='show_sheet_count',
            field=models.BooleanField(default=True, help_text='Zahrnovat počet listů do názvu produktu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='show_tags',
            field=models.BooleanField(default=True, help_text='Zahrnovat tagy do názvu produktu'),
        ),
    ]
