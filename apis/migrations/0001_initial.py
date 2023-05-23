# Generated by Django 3.2 on 2023-05-23 09:44

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
                ('title', models.CharField(max_length=150)),
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
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='uploads/preview/%Y/%m')),
                ('cooking_time', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.foodtype')),
                ('ingredients', models.ManyToManyField(to='apis.Ingredient')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='RecipeGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(help_text='load img', upload_to='uploads/gallery/%Y/%m', verbose_name='img')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.ingredientname'),
        ),
    ]
