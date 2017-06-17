from django.contrib import admin
from sign.models import Event, Guest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time', 'id']
    search_fields = ['name']   # ËÑË÷À¸
    list_filter = ['status']   # ¹ıÂËÆ÷


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'event']
    search_fields = ['realname','phone']  # ËÑË÷À¸
    list_filter = ['sign']    # ¹ıÂËÆ÷

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)


