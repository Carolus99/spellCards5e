from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Spell(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    level = models.DecimalField(max_digits=10, decimal_places=2)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    school = models.CharField(max_length=100)
    image = models.ImageField(upload_to='spell_images', default='media/default.png')

    def __str__(self):
        return self.name
