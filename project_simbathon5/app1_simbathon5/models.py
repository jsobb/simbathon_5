from django.db import models

# Create your models here.

class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 200)
    pub_date = models.CharField(max_length = 100)
    body = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[20]

