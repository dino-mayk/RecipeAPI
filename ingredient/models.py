from django.db import models


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
