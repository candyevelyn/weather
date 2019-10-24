from django.db import models

# Create your models here.
# class Search(models.Model):
#     search = models.CharField(max_length=500)
#     created = models.DateTimeField(auto_now=True) 

#     def __str__(self):
#         return '{}'.format(self.search)

#     class Meta:
#         verbose_name_plural = 'Searches'

class Extended(models.Model):
    period_name=models.CharField(max_length=500)
    img_url=models.CharField(max_length=500)
    alt_text=models.CharField(max_length=500)
    short_desc=models.CharField(max_length=50)
    temp=models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.period_name



