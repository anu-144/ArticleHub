from django.db import models

class Article(models.Model): 
    article1 = models.CharField(max_length=200)
    desc = models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.article1
