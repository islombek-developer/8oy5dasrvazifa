from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    duration = models.DurationField()

    def __str__(self) -> str:
        return self.name
    

