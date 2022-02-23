from django.db import models
from django.conf import settings
import django.utils.timezone
from django.utils.text import slugify
from .utils import generate_unique_slug


class ItemCollection(models.Model):
    CHOICES = (
        ('Alcohol', 'Alcohol'),
        ('Antiques', 'Antiques'),
        ('Art', 'Art'),
        ('Models', 'Models'),
        ('Money', 'Money'),
        ('Non-artificial objects', 'Non-artificial objects'),
        ('Printed products', 'Printed products'),
        ('Souvenirs', 'Souvenirs'),
        ('Stamps', 'Stamps'),
        ('Weapons and military', 'Weapons and military'),
        ('Other', 'Other'),
    )

    name = models.CharField("Name", max_length=150)
    slug = models.SlugField(unique=True, max_length=160)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    description = models.TextField("Description")
    created = models.DateTimeField(default=django.utils.timezone.now)
    theme = models.CharField(
        "Theme", max_length=30, choices=CHOICES, default="Other"
    )

    def save(self, *args, **kwargs):
        if self.slug:
            """edit"""
            if slugify(self.name) != self.slug:
                self.slug = generate_unique_slug(ItemCollection, self.name)
        else:
            """create"""
            self.slug = generate_unique_slug(ItemCollection, self.name)
        super(ItemCollection, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_items_count(self):
        return self.item_set.count()

    class Meta:
        db_table = "item_collection"
        verbose_name = "Collection"
        verbose_name_plural = "Collections"


class Item(models.Model):
    name = models.CharField("Name", max_length=150)
    slug = models.SlugField(unique=True, max_length=160)
    item_collection = models.ForeignKey(
        ItemCollection, on_delete=models.CASCADE
    )
    created = models.DateTimeField(default=django.utils.timezone.now)
    updated = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "item"
        verbose_name = "Item"
        verbose_name_plural = "Items"
