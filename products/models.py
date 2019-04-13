from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    Title = models.CharField(max_length=50)
    publish_date = models.DateTimeField(auto_now=True)
    Body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    def summary(self):
        return self.Body[:100]

    def publish_date_format(self):
        return self.publish_date.strftime('%b %e %Y')
