from functools import cached_property
from django.db import models
import streamlit as st

from django_pandas.managers import DataFrameManager


class Country(models.Model):
    """
    Country data
    """

    objects = DataFrameManager()

    country = models.CharField(
        "Country", max_length=255, blank=True, help_text="Name of the country"
    )
    region = models.CharField("Region", max_length=255, blank=True)
    population = models.IntegerField("Population", null=True)
    area = models.FloatField("Area (sq. mi.)", null=True)
    population_density = models.FloatField("Pop. Density (per sq. mi.)", null=True)
    coastline = models.FloatField("Coastline (coast/area ratio)", null=True)
    net_migration = models.FloatField("Net migration", null=True)
    infant_mortality = models.FloatField(
        "Infant mortality (per 1000 births)", null=True
    )
    gdp = models.FloatField("GDP ($ per capita)", null=True)
    literacy = models.FloatField("Literacy (%)", null=True)
    phones = models.FloatField("Phones (per 1000)", null=True)
    arable = models.FloatField("Arable (%)", null=True)
    crops = models.FloatField("Crops (%)", null=True)
    other = models.FloatField("Other (%)", null=True)
    climate = models.FloatField("Climate", null=True)
    birthrate = models.FloatField("Birthrate", null=True)
    deathrate = models.FloatField("Deathrate", null=True)
    agriculture = models.FloatField("Agriculture", null=True)
    industry = models.FloatField("Industry", null=True)
    service = models.FloatField("Service", null=True)

    def __str__(self):
        return str(self.country)

    @cached_property
    def column_config(self):
        columns = {}

        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                columns[field.name] = st.column_config.TextColumn(
                    label=field.verbose_name, help=field.help_text
                )

            if isinstance(field, models.IntegerField):
                columns[field.name] = st.column_config.NumberColumn(
                    label=field.verbose_name, help=field.help_text
                )

            if isinstance(field, models.FloatField):
                columns[field.name] = st.column_config.NumberColumn(
                    label=field.verbose_name, help=field.help_text
                )

        return columns
