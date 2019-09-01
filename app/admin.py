from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
	list_lisplay = ['v_type', 'amount', 'user', 'gate', 'date']


admin.site.register(Vehicle, VehicleAdmin)
admin.site.site_header = 'Jimeta Ultra Modern Market Admin'
admin.site.index_title = 'Jimeta Ultra Modern Market'
admin.site.site_title = 'JUMM'