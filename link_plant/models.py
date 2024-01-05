from django.db import models

# Create your models here.
class Profile(models.Model):
    colors = {
        ('blue','BLUE'),
        ('green','GREEN'),
        ('yellow','YELLOW'),
    }
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)
    bgcolor = models.CharField(max_length = 100, choices=colors)


    def __str__(self):
        return f"{self.name}"

class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(unique = True)
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name= 'links')

    def __str__(self):
        return f"{self.profile.name} | {self.title}"