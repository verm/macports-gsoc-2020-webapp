from django.contrib import admin

from ports.variant.models import Variant


@admin.register(Variant)
class Variant(admin.ModelAdmin):
    list_display = ("port", "variant")
