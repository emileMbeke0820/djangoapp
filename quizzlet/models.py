from django.db import models


class Vertrieb(models.Model):
    Firmenname = models.CharField(max_length=100)

    def __str__(self):
        return self.Firmenname


class auszubildende(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    Vorname = models.CharField(max_length=45)
    Nachname = models.CharField(max_length=100)
    Alter = models.IntegerField(null=True)
    Stadt = models.CharField(max_length=100)
    Geschlecht = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    Submission_date = models.DateTimeField()
    Ausbildung = models.CharField(max_length=150)
    Beziehung = models.ForeignKey(Vertrieb, on_delete=models.CASCADE)
