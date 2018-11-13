from django.db.models import CharField, BooleanField, Model

# Create your models here.


class SportKind(Model):
    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплина"
        ordering = ["Name"]

    Name = CharField(verbose_name="Название Дисциплины",
                     help_text="Название дисциплины (100м, эстафета,...)",
                     max_length=100, default="")

    def __str__(self):
        return self.Name


class Sport(Model):
    class Meta:
        verbose_name = "Вид спорта"
        verbose_name_plural = "Виды спорта"
        ordering = ["Name"]

    Name = CharField(verbose_name="Название вида спорта", max_length=100)
    Priority = BooleanField(verbose_name="Приоритетный вид спорта")
    Olympic = BooleanField(verbose_name="Олимпийский вид спорта")
    Winter = BooleanField(verbose_name="Зимний вид")

    def __str__(self):
        return self.Name


class Group(Model):
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["Name"]

    Name = CharField(verbose_name="Название группы", max_length=100)

    def __str__(self):
        return self.Name


class Place(Model):
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
        return self.City
