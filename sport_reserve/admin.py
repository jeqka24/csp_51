from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats
from .exports import SportsmanResource, ResultResource, TrainerResource

from django_extensions.admin import ForeignKeyAutocompleteAdminMixin

from .models import Event, Sportsman, Trainer, Result


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
    ordering = ["-Date"]


class ResultEventInline(admin.TabularInline):
    model = Result
    fk_name = "Event"
    extra = 1


class CommonAdmin:
    save_on_top = True
    formats = (base_formats.CSV, base_formats.TSV, base_formats.XLS, base_formats.JSON, base_formats.YAML)


class TrainerAdmin(CommonAdmin,  ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    search_fields = ['FIO']


class EventAdmin(CommonAdmin, ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    autocomplete_fields = ["Sport", "Place", "Sport"]
    list_display = ["Name", "Stage",  "Type", "Sport", ]
    list_filter = ["Type", "Sport", "DateStart", "DateEnd"]
    filter_horizontal = ["Groups", ]
    inlines = [ResultEventInline]
    search_fields = ["Name", "Place__Name"]


class SportsmanAdmin(CommonAdmin,  ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    resource_class = SportsmanResource
    search_fields = ["FIO", ]
    ordering = ["FIO", ]
    autocomplete_fields = ["Sport", "PersonalTrainer"]
    list_filter = ["Sport", ]
    list_select_related = ["Sport", ]
    list_display = ["FIO", "Sport", "age", "Degree", "PersonalTrainer"]
    list_display_links = ["FIO", "Sport", "age", "Degree", "PersonalTrainer"]
    preserve_filters = True

    inlines = [ResultSportsmanInline]


class ResultAdmin(CommonAdmin,  ForeignKeyAutocompleteAdminMixin, ImportExportActionModelAdmin):
    search_fields = ["Sportsman__FIO", "Event__Sport__Name", "Event__Name"]
    resource_class = ResultResource
    autocomplete_fields = ["Sportsman", "Event", "Group", ]
    list_filter = ["Event__Sport", "Event"]
    list_display = ["Event", "Sportsman", "Place", "Competitors"]
    fieldsets = [
        ("Соревнование", {"fields": ["Event"]}),
        ("Спортсмен", {"fields": ["Sportsman", "Group"]}),
        ("Результат", {"fields": ["Place", "Competitors", "Date", "PlaceComment"]})
    ]


admin.site.register(Event, EventAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Sportsman, SportsmanAdmin)
