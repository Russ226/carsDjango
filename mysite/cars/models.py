from django.db import models

class CarsInfo(models.Model):
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    car_pic = models.ImageField(upload_to='carPics')
    release_year = models.IntegerField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.make +" "+self.model