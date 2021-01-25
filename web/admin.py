from django.contrib import admin

# Register your models here.
from web.models import Carro


class AdminCarros(admin.ModelAdmin):
    list_display = ("nombre", "color", "imagen", "cantidad", "visible")
    list_editable = ("visible",)
    list_filter = ("color",)


admin.site.register(Carro, AdminCarros)
