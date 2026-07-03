from django.db import models

# Create your models here.
class client (models.model):
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"self.email"
    
class subscriber (models.model):
    email = models.EmailField(Unique=True)

    def __str__(self):
        return f"self.email"

