# Generated by Django 3.2 on 2023-06-12 19:27

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='uploads/images/%Y/%m')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooking_time', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=150, unique=True)),
                ('description', tinymce.models.HTMLField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.foodtype')),
                ('images', models.ManyToManyField(to='apis.RecipeImage')),
                ('ingredients', models.ManyToManyField(to='apis.Ingredient')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.ingredientname'),
        ),
    ]
