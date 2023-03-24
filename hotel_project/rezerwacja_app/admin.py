from django.contrib import admin

# Register your models here.
#from hotel_project.rezerwacja_app import models

from .models import Pokoj,Gosc,Rezerwacja

admin.site.register(Pokoj)
admin.site.register(Gosc)
admin.site.register(Rezerwacja)
