from django.db import models

# Create your models here.
class Post (models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length= 255)
    picture = models.CharField(max_length=400, blank = True)
    content = models.TextField()
    site_url = models.Charfield(max_field=400)
    vote_total = models.CharField(max_lenth=255)

    def __str__ (self):
        return self.title

        












