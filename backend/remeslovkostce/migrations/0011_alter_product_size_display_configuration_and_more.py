# Generated by Django 4.2.3 on 2023-07-11 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remeslovkostce', '0010_alter_sizedisplayconfiguration_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_display_configuration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='remeslovkostce.sizedisplayconfiguration'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_thumbnail', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='remeslovkostce.product')),
            ],
        ),
    ]
