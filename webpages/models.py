from secrets import choice
from django.db import models
CATEGORY = (
    ('comedy', "Comedy"),
    ('music', "Music"),
    ('news', "News"),
    ('education', "Education"),
    ('business', "Business"),
    ('movies', "Movies"),
)
# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    button_link = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True, choices=CATEGORY)
    youtube_link = models.URLField(default="https://www.youtube.com", blank=True, null=True)
    insta_link = models.URLField()
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")

    def __str__(self):
        return self.first_name
