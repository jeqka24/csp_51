from .models import Place, Result, Sportsman, Event, EventType, Group, Sport

from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget


class PlaceResource(resources.ModelResource):
    class Meta:
        model = Place
        fields = ("id", "Country", "Region", "City")


class SportResource(resources.ModelResource):
    class Meta:
        model = Sport
        fields = ("id", "Name", "Priority", "Olympic", "Winter")


class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
        fields = ("id", "Name")


class ResultResource(resources.ModelResource):
    class Meta:
        model = Result
        fields = (
            "id",
            "Sportsman__FIO",
            "Event__Name",
            "Group",
            "Date",
            "Place",
            "Competitors",
            "PlaceComment"
        )
        export_order = (
            "id",
            "Sportsman__FIO",
            "Event__Name",
            "Group",
            "Date",
            "Place",
            "Competitors",
            "PlaceComment"
        )
        skip_unchanged = True
        report_skipped = True


class SportsmanResource(resources.ModelResource):
    class Meta:
        model = Sportsman
        fields = (
            "id",
            "FIO",
            "Sport",
            "Degree",
            "AssignmentDate",
            "ParallelDate",
            "PersonalTrainer",
            "Organisation"
        )
        skip_unchanged = True
        report_skipped = True


class EventResource(resources.ModelResource):
    class Meta:
        model = Event
#        fields = ("")
