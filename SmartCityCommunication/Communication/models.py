from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Sender(models.Model):
    wann = models.DateTimeField(auto_now_add=True); 
    von = models.EmailField();
    grund = models.CharField(max_length=95);
    nachricht = models.TextField();
    def __str__(self):
        speichern = self.wann.strftime('%Y/%b/%d;%H:%M:%S')+ ";" + self.von + ";" + self.grund
        return speichern

class Project(models.Model):
    title = models.CharField(max_length=86)
    body = models.TextField()
    date = models.DateTimeField()
    pro = models.IntegerField(default=0)
    contra = models.IntegerField(default=0)
    rank = models.FloatField(default=0)
    
#    def save(self, *args, **kwargs):
#        self.url= slugify(self.title)
#        super(Post, self).save(*args, **kwargs)
     
    def __str__(self):
        speichern = self.date.strftime('%Y/%b/%d;%H:%M:%S')+";"+self.title
        return speichern

#class Preference(models.Model):
#    user= models.ForeignKey(User)
#    post= models.ForeignKey(Project)
#    value= models.IntegerField()
#    date= models.DateTimeField(auto_now= True)

    
#    def __str__(self):
#        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

#    class Meta:
#       unique_together = ("user", "post", "value")
        
        

        
        
 