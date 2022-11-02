from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
class Event(models.Model):
    event_name = models.CharField(max_length=300, verbose_name='Событие', unique=True, )
    class Meta:
        verbose_name_plural='События'
        verbose_name='Событие'
    def __str__(self):
        return self.event_name
class Fight(models.Model):
    first_fighter = models.ForeignKey('Fighter',on_delete=models.PROTECT, verbose_name='Первый боец',related_name='+')
    second_fighter = models.ForeignKey('Fighter',on_delete=models.PROTECT, verbose_name='Второй боец')
    number_of_rounds=models.ForeignKey('Rounds',on_delete=models.PROTECT, verbose_name='Число раундов')
    class Meta:
        verbose_name_plural='Бои'
        verbose_name='Бой'
class Rounds(models.Model):
    round_num=models.IntegerField(verbose_name='Номер раунда',validators=[MinValueValidator(0), MaxValueValidator(6)])

    class Meta:
        verbose_name_plural='Раунды'
        verbose_name='Раунд'
    def __str__(self):

        return str(self.round_num)

class Fighter(models.Model):
    name=models.CharField(max_length=200, verbose_name='Имя бойца', unique=True)
    CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский')
    ]
    gender=models.CharField(max_length=7,verbose_name='Пол', choices=CHOICES)
    class Meta:
        verbose_name_plural='Бойцы'
        verbose_name='Боец'
        ordering = ['name']
    def __str__(self):
        return self.name

class RoundStats(models.Model):
    event = models.ForeignKey('Event',on_delete=models.PROTECT, verbose_name='Событие',null=True)
    fighter = models.ForeignKey('Fighter',on_delete=models.PROTECT, verbose_name='Боец')
    opponent = models.ForeignKey('Fighter',on_delete=models.PROTECT, verbose_name='Соперник', related_name='+', null=True)
    round = models.ForeignKey('Rounds', on_delete=models.PROTECT, verbose_name='Номер раунда')
    r_protect_takedown = models.IntegerField(db_index=True,blank=True,null=True, verbose_name='Отраженных тейков за раунд',default=0,validators=[MinValueValidator(0)])
    r_strikes_head= models.IntegerField(db_index=True,blank=True,null=True, verbose_name='Удары в голову за раунд',default=0,validators=[MinValueValidator(0)])
    r_strikes_body= models.IntegerField(db_index=True, blank=True, null=True, verbose_name='Удары по туловищу  за раунд',default=0,validators=[MinValueValidator(0)])
    r_strikes_leg= models.IntegerField(blank=True, null=True, verbose_name='Удары по ногам за раунд',default=0,validators=[MinValueValidator(0)])
    class Meta:
        verbose_name_plural='Статистики лучших'
        verbose_name='Статистика за раунд лучших'

class RoundStats_all(models.Model):
    event = models.ForeignKey('Event',on_delete=models.PROTECT, verbose_name='Событие',null=True)
    fighter = models.ForeignKey('Fighter',on_delete=models.PROTECT, verbose_name='Боец')
    opponent = models.ForeignKey('Fighter',on_delete=models.PROTECT, verbose_name='Соперник', related_name='+', null=True)
    r_protect_takedown = models.IntegerField(db_index=True,blank=True,null=True, verbose_name='Сложность боя, кол-во тейков соперника',default=0,validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural='Проект антитейк'
        verbose_name='Статистика за раунд антитейк'
# Create your models here.х
class RoundStatsFighters(models.Model):
    event = models.ForeignKey('Event',on_delete=models.PROTECT, verbose_name='Событие',null=True)
    fighter = models.ForeignKey('Fighter',on_delete=models.PROTECT, verbose_name='Боец')
    opponent = models.ForeignKey('Fighter',on_delete=models.PROTECT, verbose_name='Соперник', related_name='+', null=True)
    round = models.ForeignKey('Rounds', on_delete=models.PROTECT, verbose_name='Номер раунда')
    r_protect_takedown = models.IntegerField(db_index=True,blank=True,null=True, verbose_name='Отраженных тейков за раунд',default=0,validators=[MinValueValidator(0)])
    r_strikes_head= models.IntegerField(db_index=True,blank=True,null=True, verbose_name='Удары в голову за раунд',default=0,validators=[MinValueValidator(0)])
    r_strikes_body= models.IntegerField(db_index=True, blank=True, null=True, verbose_name='Удары по туловищу  за раунд',default=0,validators=[MinValueValidator(0)])
    r_strikes_leg= models.IntegerField(blank=True, null=True, verbose_name='Удары по ногам за раунд',default=0,validators=[MinValueValidator(0)])
    class Meta:
        verbose_name_plural='Статистики всех'
        verbose_name='Статистика всех'