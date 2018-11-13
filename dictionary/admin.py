from django.contrib import admin

from .models import Place, SportKind, Sport, Group

from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats

from .exports import PlaceResource, GroupResource, SportResource
from django_extensions.admin import ForeignKeyAutocompleteAdminMixin

# Register your models here.

admin.site.site_header = "Справочник"
admin.site.site_title = "Справочник"
admin.site.empty_value_display = '- нет -'

admin.autodiscover()


class CommonAdmin:
    save_on_top = True
    formats = (base_formats.CSV, base_formats.TSV, base_formats.XLS, base_formats.JSON, base_formats.YAML)


class SportKindAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    search_fields = ["Name", ]


class SportAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = SportResource
    search_fields = ["Name", ]
    list_display = ["Name", "Priority", "Olympic", "Winter"]
    list_filter = ["Priority", "Olympic", "Winter"]


class GroupAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = GroupResource
    search_fields = ["Name", ]


class PlaceAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = PlaceResource
    list_display = ["Country", "Region", "City"]
    list_filter = ["Country", "Region"]
    search_fields = ["Country", "Region", "City"]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(SportKind, SportKindAdmin)
