from django.db import models

from django.utils import timezone

from .utils import generate_uuid, generate_color, color_code_validator


class Category(models.Model):
    guid = models.CharField(max_length=32, primary_key=True, editable=False, default=generate_uuid)
    title = models.CharField(max_length=64, null=False, blank=False)
    color_code = models.CharField(max_length=7, default=generate_color, validators=[color_code_validator])
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    modified_at = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Item(models.Model):
    guid = models.CharField(max_length=32, primary_key=True, editable=False, default=generate_uuid)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, db_column='category_guid', on_delete=models.CASCADE)
    metadata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    modified_at = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.title


class Rank(models.Model):
    data = models.TextField()


class AuditLog(models.Model):
    log = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.log

    class Meta:
        verbose_name_plural = 'Audit Logs'
        verbose_name = 'Audit Log'
