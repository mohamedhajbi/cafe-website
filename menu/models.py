from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255)
    img=models.ImageField(upload_to="categories_imgs/",null=True)
    def __str__(self):
        return self.name
    class Meta:
	    verbose_name_plural='Categories'

    def image_tag(self):    
        return mark_safe('<img src ="%s" width="80" />'% (self.img.url))

class List(models.Model):
    categories=models.ForeignKey(Categories, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=150)
    prix=models.IntegerField(default=0)
    img=models.ImageField(upload_to="list_imgs/",null=True)
    
    def __str__(self):
        return self.name
    def image_tag(self):    
        return mark_safe('<img src ="%s" width="80" />'% (self.img.url)) 