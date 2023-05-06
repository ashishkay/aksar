from django.db import models

class Donor(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  blood_group = models.CharField(max_length=255)
  Donated_date = models.DateTimeField(auto_now=True, blank=True)
  phone = models.IntegerField(null=True)
  age = models.IntegerField(null=True)
  address = models.CharField(max_length=255, null=True)
  volume_donated = models.IntegerField(null=True)

  def __str__(self):
    return self.first_name + ' ' + self.last_name