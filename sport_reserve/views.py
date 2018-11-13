from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Trainer, Sportsman, Event, Result
from django.views.generic.base import TemplateView

from django.core import serializers

# Create your views here.


class SportsmenView(ListView):
    model = Sportsman
    queryset = Sportsman.objects.order_by("FIO")


class SportsmanView(DetailView):
    model = Sportsman


class TrainersView(ListView):
    model = Trainer
    queryset = Trainer.objects.order_by("FIO")


class TrainerView(DetailView):
    model = Trainer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sportsman_list'] = Sportsman.objects.filter(PersonalTrainer=kwargs['object'].id).order_by('FIO')
        return context


class EventsView(ListView):
    model = Event
    queryset = Event.objects.order_by("Name")


class EventView(DetailView):
    model = Event
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)

#        context['sportsman_list'] = Result.objects.filter(=kwargs['object'].id).order_by('FIO')
#        return context


class ResultsView(ListView):
    model = Result

class ResultView(DetailView):
    model = Result
    queryset = Result

class indexView(TemplateView):
    template_name = "index.html"


def SportAndSportsman(request):
    pass


# Квартальный отчет отдела
def QuaterlyReport(request):
    pass


# Недельный отчет отдела
def WeekdlyReport(request):
    pass


# Отчет по призёрам ПР и спартакиад
def WinnersReport(request):
    result = models.Result.objects.filter()
    pass


# Лучшие результаты за квартал
def QuaterlyBestReport(request):
    pass


#