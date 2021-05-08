from django.contrib import admin
from .models import Parts, TestPart


class PartAdmin(admin.ModelAdmin):
    list_display = ('part_name', 'part_id')
    list_display_links = ('part_name',)
    list_editable = ('part_id',)
    ordering = ('part_name',)


class TestPartAdmin(admin.ModelAdmin):
    list_display = ('part_name', 'part_id')
    list_display_links = ('part_name',)
    list_editable = ('part_id',)
    ordering = ('part_name',)


admin.site.register(Parts, PartAdmin)
admin.site.register(TestPart, TestPartAdmin)

