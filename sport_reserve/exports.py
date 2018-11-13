from .models import Result, Sportsman, Event, Trainer
from import_export import fields, resources


class ResultResource(resources.ModelResource):
    class Meta:
        model = Result
        skip_unchanged = True
        report_skipped = True


class SportsmanResource(resources.ModelResource):
    class Meta:
        model = Sportsman
        skip_unchanged = True
        report_skipped = True


class EventResource(resources.ModelResource):
    class Meta:
        model = Event


class TrainerResource(resources.ModelResource):
    class Meta:
        model = Trainer
        skip_unchanged = True
        report_skipped = True
