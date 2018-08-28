from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats
from .exports import PlaceResource, SportsmanResource, ResultResource, GroupResource, SportResource

from django_extensions.admin import ForeignKeyAutocompleteAdminMixin

from .models import Event, EventType, Place, Sport, SportKind, \
    Sportsman, Trainer, Result, Group


admin.site.site_header = "Спортивный резерв Мурманской области"
admin.site.site_title = "Спортивный резерв Мурманской области"
admin.site.empty_value_display = '- нет -'

# Register your models here.
# Basic registering

admin.autodiscover()
# Custom forms for tables


# Filtering:
# list_filter = [("field-name", admin.RelatedOnlyFieldListFilter),]


class ResultSportsmanInline(admin.TabularInline):
    model = Result
    fk_name = "Sportsman"
    extra = 1


class ResultEventInline(admin.TabularInline):
    model = Result
    fk_name = "Event"
    extra = 1


class CommonAdmin:
    save_on_top = True


class EventTypeAdmin(CommonAdmin, admin.ModelAdmin):
    search_fields = ["Name", ]


class TrainerAdmin(CommonAdmin, admin.ModelAdmin):
    autocomplete_fields = ["Sport"]
    search_fields = ["FIO", ]


class EventAdmin(CommonAdmin, admin.ModelAdmin):
    autocomplete_fields = ["Sport", "Type", "Place"]
    search_fields = ["Name", ]
    list_display = ["Name", "Stage",  "Type", "Sport", ]
    list_filter = ["Type", "Sport", ]
    filter_horizontal = ["Groups"]

    inlines = [ResultEventInline]


class SportKindAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, admin.ModelAdmin):
    search_fields = ["Name"]


class SportAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = SportResource
    search_fields = ["Name", ]
    list_display = ["Name", "Priority", "Olympic", "Winter"]
    list_filter = ["Priority", "Olympic", "Winter"]
    formats = (base_formats.CSV, base_formats.TSV, base_formats.XLS)


class GroupAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = GroupResource
    search_fields = ["Name"]
    formats = (base_formats.CSV, base_formats.TSV, base_formats.XLS)


class SportsmanAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = SportsmanResource
    search_fields = ["FIO", ]
    autocomplete_fields = ["Sport", "PersonalTrainer"]
    list_filter = ["Sport"]
    list_display = ["FIO", "Sport", "age", "Degree", "PersonalTrainer"]
    list_display_links = ["FIO", "Sport", "age", "Degree", "PersonalTrainer"]
    formats = (base_formats.CSV, base_formats.TSV, base_formats.XLS)
    preserve_filters = True

    inlines = [ResultSportsmanInline]

class ResultAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = ResultResource
    autocomplete_fields = ["Sportsman", "Event", "Group", "Sport", "SportKind"]
    list_filter = ["Event__Sport", "Event"]
    list_display = ["Event", "Sportsman", "Place", "Competitors"]
    formats = (base_formats.CSV, base_formats.TSV, base_formats.XLS)
    # fields = ["Sport", "Sportsman", "Event", "Group", "Place", "Competitors", "PlaceComment"]
    fieldsets = [
        ("Соревнование", {"fields": ["Sport", "Event"]}),
        ("Спортсмен", {"fields": ["Sportsman", "SportKind", "Group"]}),
        ("Результат", {"fields": ["Place", "Competitors", "Date", "PlaceComment"]})
    ]



class PlaceAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = PlaceResource
    list_display = ["Country", "Region", "City"]
    list_filter = ["Country", "Region"]
    search_fields = ["Country", "Region", "City"]
    formats = (base_formats.CSV, base_formats.TSV, base_formats.XLS)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Sportsman, SportsmanAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(SportKind, SportKindAdmin)
