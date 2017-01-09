from django.db import models

# Create your models here.
class Spell(models.Model):
    name = models.CharField(max_length=100)
    level = models.DecimalField(max_digits=10, decimal_places=2)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    school = models.CharField(max_length=100)
    img_url = models.CharField(max_length = 100, default="https://www.cleverfiles.com/howto/wp-content/uploads/2016/08/mini.jpg")

    def __str__(self):
        return self.name
