from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

#books
class Book(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(null=True)
    detail=FroalaField(theme='dark')
    img=models.ImageField(upload_to="books/",null=True)

    def __str__(self):
        return self.title

    def image_tag(self):    
     return mark_safe('<img src ="%s" width="80" />'% (self.img.url))


class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
    content=models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)




    
#gallery

class EventsImage(models.Model):
    title =models.CharField(max_length=255, blank=True)
    alt_text=models.CharField(max_length=150)
    img=models.ImageField(upload_to="event_imgs/",null=True)
    class Meta:
	    verbose_name_plural='Event Images'
    def __str__(self):
        return self.alt_text

    def image_tag(self):    
     return mark_safe('<img src ="%s" width="80" />'% (self.img.url))
    