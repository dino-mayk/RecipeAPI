from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Ingredient(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class FoodType(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Recipe(models.Model):
    ingredients = models.JSONField()
    food_type = models.ForeignKey(
        FoodType,
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        null=True,
    )
    cooking_time = models.PositiveIntegerField()
    title = models.CharField(
        max_length=150,
    )
    description = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)

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
        return 'now img'

    img_tmb.short_description = 'preview'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']


class RecipeGallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/gallery/%Y/%m',
        verbose_name="img",
        help_text='load img'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'no img'

    img_tmb.short_description = 'photos'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url
