# Generated by Django 2.2.2 on 2019-06-22 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=95, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=95, verbose_name='Nombre del producto')),
                ('image', models.CharField(max_length=500, verbose_name='Imagen de producto')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='inventory.Category', verbose_name='Categoria del producto')),
            ],
        ),
    ]