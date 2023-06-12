from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class FoodType(models.Model):

    title = models.CharField(
        max_length=150,
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class IngredientName(models.Model):

    title = models.CharField(
        max_length=150,
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Ingredient(models.Model):

    ingredient_name = models.ForeignKey(
        IngredientName,
        on_delete=models.CASCADE,
    )
    quantity = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return '%s: %s' % (self.quantity, self.ingredient_name)


class RecipeImage(models.Model):

    image = models.ImageField(
        upload_to='uploads/images/%Y/%m',
        null=True,
    )

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo,
            '300x300',
            crop='center',
            quality=51,
        )

    def img_tmb(self):
        if self.photo:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'no img'

    img_tmb.short_description = 'image'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.image.url


class Recipe(models.Model):

    ingredients = models.ManyToManyField(Ingredient)
    images = models.ManyToManyField(RecipeImage)
    food_type = models.ForeignKey(
        FoodType,
        on_delete=models.CASCADE,
    )
    cooking_time = models.PositiveIntegerField()
    title = models.CharField(
        max_length=150,
        unique=True,
    )
    description = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']
