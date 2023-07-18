from django.db import models


class FoodType(models.Model):

    title = models.CharField(
        max_length=150,
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
