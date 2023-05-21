from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Ingredient(models.Model):
    title = models.CharField(
        'заголовок',
        max_length=150,
    )
    quantity = models.CharField(
        'количество',
        max_length=150,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'


class FoodType(models.Model):
    title = models.CharField(
        'заголовок',
        max_length=150,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

        verbose_name = 'тип блюда'
        verbose_name_plural = 'типы блюд'


class Recipe(models.Model):
    ingredient = models.ManyToManyField(
        Ingredient,
        verbose_name="ингредиенты",
    )
    food_type = models.ForeignKey(
        FoodType,
        on_delete=models.CASCADE,
        verbose_name="категория",
        help_text="выберете тип блюда",
    )
    photo = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name='картинка',
        help_text='загрузите картинку',
        null=True,
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name='время приготовления(в минутах)',
    )
    title = models.CharField(
        'заголовок',
        max_length=150,
    )
    description = HTMLField(
        verbose_name='описание',
        help_text='введите ваше описание рецепта',
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
        help_text="дата создания",
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
        return 'нет изображений'

    img_tmb.short_description = 'превьюшки'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']

        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'


class RecipeGallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/gallery/%Y/%m',
        verbose_name="картинка",
        help_text='загрузите картинку'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="рецепт",
        help_text='выберете рецепт'
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'фотогалерея'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "фотографию рецепта"
        verbose_name_plural = "фотогалерея рецептов"
