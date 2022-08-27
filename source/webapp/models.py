from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

CATEGORY_CHOICES = [('Samsung s22 ultra', 'Samsung s22 ultra'),
                    ('Samsung Galaxy Tab', 'Samsung Galaxy Tab'),
                    ('SAMSUNG 55QN700B 55', 'SAMSUNG 55QN700B 55'),
                    ('Galaxy Watch4 Classic', 'Galaxy Watch4 Classic')
                    ]

DEFAULT_CHOICES = [
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1),
]


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Название")
    description = models.TextField(max_length=2000, blank=True, verbose_name="Описание")
    category = models.CharField(max_length=30, blank=False, verbose_name="Категория", choices=CATEGORY_CHOICES)
    picture = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Картинка", default='/images/photo-1.jpg')

    def __str__(self):
        return f"{self.id}. {self.name}: {self.description}.{self.category}.{self.picture}"

    def get_absolute_url(self):
        return reverse("webapp:detail_view", kwargs={"pk": self.pk})


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, related_name="reviews",
                             verbose_name='Автор')
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE,
                                related_name="reviews", verbose_name="Продукт")
    description_reviews = models.TextField(max_length=3000, blank=False, verbose_name="Отзыв")
    grade = models.IntegerField(blank=False, choices=DEFAULT_CHOICES, verbose_name="Оценка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    moderated = models.BooleanField(default=True, verbose_name="Промодерировать")

    def __str__(self):
        return f"{self.id}. {self.user}: {self.product}.{self.description_reviews}.{self.grade}.{self.moderated}"
