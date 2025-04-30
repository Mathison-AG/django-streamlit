import pandas as pd
import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import test data"

    def handle(self, *args, **options):
        from ...models import Country

        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        filename = os.path.join(
            base_dir, "management/commands/data/countries_of_the_world.csv"
        )
        dataset = pd.read_csv(
            filename, sep=",", encoding="utf-8", quotechar='"'
        ).fillna(0)

        Country.objects.all().delete()

        countries = []

        for _, row in dataset.iterrows():
            country = Country(
                country=row["Country"],
                region=row["Region"],
                population=row["Population"],
                area=int(row["Area (sq. mi.)"]),
                population_density=row["Pop. Density (per sq. mi.)"],
                coastline=row["Coastline (coast/area ratio)"],
                net_migration=row["Net migration"],
                infant_mortality=row["Infant mortality (per 1000 births)"],
                gdp=int(row["GDP ($ per capita)"]),
                literacy=row["Literacy (%)"],
                phones=row["Phones (per 1000)"],
                arable=row["Arable (%)"],
                crops=row["Crops (%)"],
                other=row["Other (%)"],
                climate=row["Climate"],
                birthrate=row["Birthrate"],
                deathrate=row["Deathrate"],
                agriculture=row["Agriculture"],
                industry=row["Industry"],
                service=row["Service"],
            )

            countries.append(country)

        Country.objects.bulk_create(countries)

        self.stdout.write(self.style.SUCCESS("Test data imported successfully"))
