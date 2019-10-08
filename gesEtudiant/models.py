from django.db import models

# Create your models here.


class Etudiant(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    datenaiss = models.DateField()

    def is_mouhamed(self):
        return self.prenom == "mouhamed"