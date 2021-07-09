from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="İsim")
    last_name = models.CharField(max_length=50, verbose_name="Soyisim")
    number = models.IntegerField(verbose_name="Numara")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")
    age = models.CharField(max_length=3, verbose_name="Yaş")


    def __str__(self):
        return self.first_name
