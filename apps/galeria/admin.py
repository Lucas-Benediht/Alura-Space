from django.contrib import admin
from apps.galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id","nome")
    #Precisa ser uma tupla
    search_fields = ("nome",)
    list_filter = ("categoria", "usuario",)
    #checkbox
    list_editable = ("publicada",)
    list_per_page = 5
    
    
    
admin.site.register(Fotografia, ListandoFotografias)
