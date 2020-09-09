from django.db import models

# Create your models here.


class UserModel(models.Model):
    user_email = models.EmailField(max_length=254)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.user_email


