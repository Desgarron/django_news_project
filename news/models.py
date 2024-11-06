from django.db import models
from django.urls import reverse
from pkg_resources import require


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title_new")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Is published")
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("view_new", kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
        ordering = ["-created_at"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Title_category")

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]
