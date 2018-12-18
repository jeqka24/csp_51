from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.db.models import Count

from django.template.response import TemplateResponse

from .models import Trainer, Sportsman, Event, Result

import datetime

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

class WeeklyReport(TemplateView):
    """
    Спорт -> Мероприятие -> Результат
    """

    template_name = "reports/weekly.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        (year, week, _) = datetime.date.today().isocalendar()

        if "year" in kwargs:
            year = int(kwargs["year"])

        (_, lastweek, _) = datetime.date(year, 12, 31).isocalendar()

        if "week" in kwargs:
            week = int(kwargs["week"])
        if week > lastweek:
            week = lastweek




        DateStart = datetime.datetime.strptime(" ".join([str(year), str(week), "1"]), '%G %V %u')
        DateEnd = datetime.datetime.strptime(" ".join([str(year), str(week), "7"]), '%G %V %u')
        context['results'] = Result.objects.filter(Date__range=[DateStart, DateEnd]).order_by("Event__Sport__Name").order_by("-Date")
        context['Date_start'] = DateStart.strftime("%G-%m-%d")
        context['Date_end'] = DateEnd.strftime("%G-%m-%d")
        context['weeks'] = range(1, 53)
        context['week'] = int(week)
        context['year'] = int(year)
        context['lastweek'] = int(lastweek)
        return context


# Квартальный отчет отдела
class QuaterlyReport(TemplateView):
    """
    Спорт -> Мероприятие -> Результат
    """

    template_name = "reports/quarterly.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        (year, month) = (today.year, today.month)

        quarter = (month - 1) // 4

        if "quarter" in kwargs:
            quarter = int(kwargs["quarter"]) - 1
        if "year" in kwargs:
            year = int(kwargs["year"])

        QTable = {
            0: (datetime.date(year, 1, 1), datetime.date(year, 3, 31)),
            1: (datetime.date(year, 4, 1), datetime.date(year, 6, 30)),
            2: (datetime.date(year, 7, 1), datetime.date(year, 9, 30)),
            3: (datetime.date(year, 10, 1), datetime.date(year, 12, 31)),
        }

        print("DateEnd", " ".join([str(year), str(quarter*3+3), "31"]))

        DateStart, DateEnd = QTable[quarter]

        context['results'] = Result.objects.filter(Date__range=[DateStart, DateEnd]).order_by("-Date").order_by("Event__Sport__Name")
        context['Date_start'] = DateStart.strftime("%Y-%m-%d")
        context['Date_end'] = DateEnd.strftime("%Y-%m-%d")
        context['quarters'] = range(1, 5)
        context['quarter'] = str(quarter)
        context['year'] = str(year)
        return context

# Зимние виды спорта за сезон
def WinterSportReport(request):
    pass


# Летние виды спорта за сезон
def SummerSportReport(request):
    pass


# Лучшие результаты за квартал
def QuaterlyBestReport(request):
    pass


# Отчет по призёрам ПР и спартакиад
def ChampionsReport(request):
    pass

#