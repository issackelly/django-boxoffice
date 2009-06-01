from django.contrib import admin
from models import TicketGroup, Ticket

class TicketGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'registration_open']

admin.site.register(TicketGroup, TicketGroupAdmin)
admin.site.register(Ticket)
