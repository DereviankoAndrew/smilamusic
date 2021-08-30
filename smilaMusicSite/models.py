from django.db import models

# Create your models here.

class StudentsAmount(models.Model):
    amount = models.CharField(max_length=200)

    def __str__(self):
        return ('Кількість учнів: ' + str(self.amount))

class StudentRequest(models.Model):
    age = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):

        return (self.phone_number)


class PhoneNumbers(models.Model):
    drums = models.CharField(max_length=200)
    e_guitar = models.CharField(max_length=200)
    bass_guitar = models.CharField(max_length=200)
    vocals = models.CharField(max_length=200)
    piano = models.CharField(max_length=200)

    def __str__(self):
        return ('Телефони викладачів')


