from django.db.models import Model, PROTECT
from django.db.models import CharField, ForeignKey, DateField, ManyToManyField, \
    BooleanField, IntegerField, FloatField, ImageField

from os.path import join as opj
from datetime import date


def get_photo_path(instance, filename):
    return opj("images", str(instance.id), filename)


class BaseModel(Model):
    class Meta:
        pass


class SportKind(BaseModel):
    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплина"
        ordering = ["Name"]

    Name = CharField(verbose_name="Название Дисциплины",
                     help_text="Название дисциплины (100м, эстафета,...)",
                     max_length=100, default="")

    def __str__(self):
        return self.Name


class Sport(BaseModel):
    class Meta:
        verbose_name = "Вид спорта"
        verbose_name_plural = "Виды спорта"
        ordering = ["Name"]

    Name = CharField(verbose_name="Название вида спорта", max_length=100)
    # Kind = ForeignKey(SportKind, verbose_name="Тип спорта", on_delete=PROTECT, blank=False, null=True)
    Priority = BooleanField(verbose_name="Приоритетный вид спорта")
    Olympic = BooleanField(verbose_name="Олимпийский вид спорта")
    Winter = BooleanField(verbose_name="Зимний вид")

    def __str__(self):
        return self.Name


class Group(BaseModel):
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["Name"]

    Name = CharField(verbose_name="Название группы", max_length=100)

    def __str__(self):
        return self.Name


class EventType(BaseModel):
    class Meta:
        verbose_name = "Вид мерприятия"
        verbose_name_plural = "Виды мероприятий"

    Name = CharField(verbose_name="Вид мероприятия",
                     help_text="Тренировочные, Всероссийские, Международные",
                     max_length=100)

    def __str__(self):
        return self.Name


class Trainer(BaseModel):
    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    FIO = CharField(verbose_name="Фамилия, Имя, Отчество", help_text="ФИО тренера", max_length=100)
    Sport = ForeignKey(Sport, verbose_name="Вид спорта",
                       help_text="Вид спорта, которым тренер занимается в данный момент", on_delete=PROTECT)
    Phone1 = CharField(verbose_name="Рабочий телефон", blank=True, null=True, max_length=100)
    Phone2 = CharField(verbose_name="Мобильный телефон", blank=True, null=True, max_length=100)
    Email = CharField(verbose_name="e-mail", blank=True, null=True, max_length=100)

    def __str__(self):
        return self.FIO


class Sportsman(BaseModel):
    class Meta:
        verbose_name = "Спортсмен"
        verbose_name_plural = "Спортсмены"

    FIO = CharField(verbose_name="Фамилия, Имя, Отчество", help_text="ФИО спортсмена", max_length=100)
    Photo = ImageField(upload_to=get_photo_path, verbose_name="Фото",
                       help_text="Фото спортсмена", null=True, blank=True)
    Birthday = DateField(verbose_name="День рождения", help_text="День рождения", null=True, blank=True)
    Sport = ForeignKey(Sport, verbose_name="Вид спорта", help_text="Вид спорта, которым занимается спортсмен",
                       on_delete=PROTECT, null=True)
    Degree = CharField(verbose_name="Разряд/звание", help_text="Разряд или звание, присвоенные спорстмену",
                       blank=True, null=True, max_length=100)
    AssignmentDate = DateField(verbose_name="Срок окончания трудового договора", blank=True, null=True)
    ParallelDate = DateField(verbose_name="Срок окончания параллельного зачета", blank=True, null=True)
    PersonalTrainer = ForeignKey(Trainer, verbose_name="Текущий тренер", on_delete=PROTECT, blank=True, null=True)
    Organisation = CharField(verbose_name="ФСО", help_text="Физкультурно-спортивная организация", blank=True, null=True,
                             max_length=100)

    def age(self):
        a = self.Birthday
        if a:
            result = str(date.today().year - a.year)
        else:
            result = None
        return result

    def __str__(self):
        return self.FIO


class Place(BaseModel):
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
        ordering = ["Country", "Region", "City"]

    Country = CharField(verbose_name="Страна",
                        help_text="Страна проведения мероприятия или соревнования",
                        max_length=50)
    Region = CharField(verbose_name="Область",
                       help_text="Регион, область, республика, провинция...",
                       blank=True, null=True,
                       max_length=50)
    City = CharField(verbose_name="Город",
                     help_text="Населенный пункт (город)",
                     max_length=50)

    def __str__(self):
        return "{place.City}".format(place=self)


class Event(BaseModel):
    class Meta:
        verbose_name = "Мерприятие"
        verbose_name_plural = "Мероприятия"

    Name = CharField(verbose_name="Название мероприятия", max_length=100)

    Place = ForeignKey(Place,
                       verbose_name="Место проведения",
                       help_text="Место проведения мероприятия или соревнования",
                       on_delete=PROTECT)
    Type = ForeignKey(EventType,
                      verbose_name="Вид мероприятия",
                      help_text="Тренировочные, Всероссийские, Международные",
                      on_delete=PROTECT)
    Sport = ForeignKey(Sport,
                       verbose_name="Вид спорта",
                       help_text="Вид спорта", on_delete=PROTECT)

    Groups = ManyToManyField(Group, verbose_name="Группы",
                             help_text="Группы")

    Stage = CharField(verbose_name="Этап соревнований", null=True, blank=True, max_length=30)
    DateStart = DateField(verbose_name="Дата начала мероприятия")
    DateEnd = DateField(verbose_name="Дата окончания мероприятия")
    EKP = CharField(verbose_name="№ ЕКП", null=True, blank=True, max_length=30)
    FactCost = FloatField(verbose_name="Фактические расходы", null=True, blank=True)

    def __str__(self):
        return "{event.Name}, {event.Place}".format(event=self)

def results(self):
    pass

class Result(BaseModel):
    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"

    # def __init__(self, *args, **kv):
    #     print(kv, args)
    #     super().__init__(self, *args, **kv)


    Sport = ForeignKey(Sport, on_delete=PROTECT)

    Event = ForeignKey(Event, verbose_name="Соревнование", related_name="Events",
                       on_delete=PROTECT)

    Sportsman = ForeignKey(Sportsman, verbose_name="Спортсмен", on_delete=PROTECT)

    Group = ForeignKey(Group, verbose_name="Группа", on_delete=PROTECT)
    SportKind = ForeignKey(SportKind, verbose_name="Дисциплина", related_name="Results",
                           on_delete=PROTECT)
    Date = DateField(verbose_name="Дата результата")
    Place = IntegerField(verbose_name="Занятое место")
    PlaceComment = CharField(verbose_name="Занятое место (комментарии)", blank=True, null=True, max_length=100)
    Competitors = IntegerField(verbose_name="Количество участников")

    def __str__(self):
        return "{result.Event} - {result.Sportsman.FIO}, {result.Date}, занято {result.Place} место из {result.Competitors}".format(result=self)
