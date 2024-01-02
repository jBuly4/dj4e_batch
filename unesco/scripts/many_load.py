import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, Iso, Region, Site, State


def run():
    with open('./unesco/data/whc-sites-2018-clean.csv') as fhand:
        reader = csv.reader(fhand)
        next(reader)  # Advance past the header

        Category.objects.all().delete()
        Iso.objects.all().delete()
        Region.objects.all().delete()
        State.objects.all().delete()
        Site.objects.all().delete()

        # name,description,justification,year,longitude,latitude,
        # area_hectares,category,state,region,iso

        for row in reader:
            print(row)
            name = row[0]
            description = row[1]
            justification = row[2]
            try:
                year = int(row[3])
            except:
                year = None

            try:
                longitude = float(row[4])
            except:
                longitude = None

            try:
                latitude = float(row[5])
            except:
                latitude = None

            try:
                area_hectares = float(row[6])
            except:
                area_hectares = None
            category, _ = Category.objects.get_or_create(name=row[7])
            state, _ = State.objects.get_or_create(name=row[8])
            region, _ = Region.objects.get_or_create(name=row[9])
            iso, _ = Iso.objects.get_or_create(name=row[10])

            site = Site(
                    name=name,
                    year=year,
                    latitude=latitude,
                    longitude=longitude,
                    description=description,
                    justification=justification,
                    area_hectares=area_hectares,
                    category=category,
                    region=region,
                    iso=iso,
                    state=state
            )
            site.save()
