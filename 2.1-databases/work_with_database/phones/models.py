from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # Добавляет требуемые поля
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()

    # Автоматически создает поле 'slug' при сохранении в базу данных новой записи модели
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

