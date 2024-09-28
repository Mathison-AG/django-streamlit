from django.db import models


class Country(models.Model):
    """
    Country
    Region
    Population
    Area (sq. mi.)
    Pop. Density (per sq. mi.)
    Coastline (coast/area ratio)
    Net migration
    Infant mortality (per 1000 births),GDP ($ per capita)
    Literacy (%)
    Phones (per 1000)
    Arable (%)
    Crops (%)
    Other (%)
    Climate
    Birthrate
    Deathrate
    Agriculture
    Industry
    Service
    """

    country = models.CharField("Country", max_length=255, blank=True)
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
