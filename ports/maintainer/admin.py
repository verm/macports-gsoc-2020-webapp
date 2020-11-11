from django.contrib import admin

from ports.maintainer.models import Maintainer


@admin.register(Maintainer)
class Maintainer(admin.ModelAdmin):
    list_display = ("github", "name", "domain")
