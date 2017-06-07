from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


def create_company_slug(instance, new_slug=None):
    slug = slugify(instance.name)

    if new_slug is not None:
        slug = new_slug

    qs = Company.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_company_slug(instance, new_slug=new_slug)
    return slug


def company_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_company_slug(instance)

pre_save.connect(company_pre_save_receiver, sender=Company)
