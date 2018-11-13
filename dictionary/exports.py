from .models import Place, Group, Sport, SportKind
from import_export import resources


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


class SportKindResource(resources.ModelResource):
    class Meta:
        model = SportKind
        fields = ("id", "Name")
