from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.db.models import Count

from .models import Trainer, Sportsman, Event, Result

from django.core import serializers

# Create your views here.


class SportsmenView(ListView):
    model = Sportsman
    queryset = Sportsman.objects.order_by("FIO")



class SportsmanView(DetailView):
    model = Sportsman

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['results_list'] = Result.objects.filter(Sportsman_id=kwargs['object'].id).order_by('-Date')
        return context



class TrainersView(ListView):
    model = Trainer
    queryset = Trainer.objects.order_by("FIO")


class TrainerView(DetailView):
    model = Trainer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

#        sportsmen = Sportsman.objects.filter(PersonalTrainer=kwargs['object'].id)
#       get the results from the events when this trainer attended to
#       1. choose events, where this trainers take position
#       2. choose results that was achieved on those events

#       choose a sportsmen he trains everyday
        context['result_list'] = Result.objects.filter(Sportsman__PersonalTrainer=kwargs['object'].id)
        return context


class EventsView(ListView):
    model = Event
    queryset = Event.objects.order_by("Name")


class EventView(DetailView):
    model = Event
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['results_list'] = Result.objects.filter(Event=kwargs['object'].id).order_by('Date', 'Group', 'Place')
        return context


class ResultsView(ListView):
    model = Result
    queryset = Result.objects.order_by("-Date")
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        r = Result.objects.all()
        if 'end-date' in kwargs:
            r = r.filter(Result__lt=kwargs['end-date'])
        if 'start-date' in kwargs:
            r = r.filter(Result__gt=kwargs['start-date'])
        context['results_list'] = r
        return context


class ResultView(DetailView):
    model = Result



class indexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results_count'] = Result.objects.count()
        context['events_count'] = Event.objects.count()
        context['sportsmen_count'] = Sportsman.objects.count()
        context['trainers_count'] = Trainer.objects.count()
        return context



# Недельный отчет отдела
def WeekdlyReport(request):
    pass

# Квартальный отчет отдела
def QuaterlyReport(request):
    pass


def WinterSportReport(request):
    pass

# Лучшие результаты за квартал
def QuaterlyBestReport(request):
    pass

# Отчет по призёрам ПР и спартакиад
def WinnersReport(request):
    pass

#