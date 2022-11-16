from django.db import models


# Create your models here.


class Release(models.Model):
    reason = models.CharField(max_length=250)
    pub_date = models.DateTimeField("Data published")

    def __str__(self):
        return self.reason

class Products(models.Model):
    release = models.ForeignKey(Release,on_delete=models.CASCADE,default=None)
    katalog = models.CharField(max_length=250)
    model = models.CharField(max_length=250)

    def __str__(self):
        return self.katalog

