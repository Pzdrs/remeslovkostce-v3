# Generated by Django 4.2.3 on 2023-07-10 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_masculine', models.CharField(max_length=64)),
                ('label_feminine', models.CharField(max_length=64)),
                ('label_neuter', models.CharField(max_length=64)),
                ('hex', models.CharField(blank=True, default='FFFFFF', max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSizeLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_masculine', models.CharField(max_length=64)),
                ('label_feminine', models.CharField(max_length=64)),
                ('label_neuter', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_count', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('depth', models.PositiveIntegerField()),
                ('unit', models.CharField(choices=[('mm', 'milimetr'), ('cm', 'centimetr'), ('m', 'metr')], default='cm', max_length=2)),
                ('label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='remeslovkostce.productsizelabel')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('M', 'mužský'), ('F', 'ženský'), ('N', 'střední')], max_length=1)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remeslovkostce.productcategory')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='remeslovkostce.productcolor')),
            ],
        ),
    ]
