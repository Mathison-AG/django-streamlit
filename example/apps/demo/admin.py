from django.contrib import admin

from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "region",
        "population",
        "area",
        "population_density",
        "coastline",
        "net_migration",
        "infant_mortality",
        "gdp",
        "literacy",
        "phones",
        "arable",
        "crops",
        "other",
        "climate",
        "birthrate",
        "deathrate",
        "agriculture",
        "industry",
        "service",
    )
    search_fields = ("country",)
    list_filter = ("region",)
    ordering = ("country",)
