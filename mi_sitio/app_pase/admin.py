from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as app_pase


admin.site.register(app_pase.Lugar, LeafletGeoAdmin)

