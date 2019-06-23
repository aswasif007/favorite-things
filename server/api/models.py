from django.db import models

from jsonfield import JSONField

from .utils import generate_uuid, generate_color, color_code_validator, RankHandler


class Category(models.Model):
    guid = models.CharField(max_length=32, primary_key=True, editable=False, default=generate_uuid)
    title = models.CharField(max_length=64, null=False, blank=False)
    color_code = models.CharField(max_length=7, default=generate_color, validators=[color_code_validator])
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']


class Item(models.Model):
    guid = models.CharField(max_length=32, primary_key=True, editable=False, default=generate_uuid)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, db_column='category_guid', on_delete=models.CASCADE)
    metadata = JSONField(null=True, blank=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.title

    @property
    def rank(self):
        rank_obj = Rank.objects.first()
        return rank_obj.data.get(self.guid)

    def save(self, *args, **kwargs):
        rank_obj = Rank.objects.first()

        if not rank_obj:
            rank_obj = Rank.objects.create()

        rank_obj.insert_item(self.guid)
        rank_obj.save()

        return super(Item, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        rank_obj = Rank.objects.first()

        rank_obj.delete_item(self.guid)
        rank_obj.save()

        return super(Item, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class Rank(models.Model, RankHandler):
    data = JSONField(default={})


class AuditLog(models.Model):
    log = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.log

    class Meta:
        verbose_name_plural = 'Audit Logs'
        verbose_name = 'Audit Log'
        ordering = ['-created_at']
