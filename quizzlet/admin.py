from django.contrib import admin

from .models import auszubildende


@admin.register(auszubildende)
class Azubi(admin.ModelAdmin):
    pass
