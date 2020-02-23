from django.db import models
# Create your models here.

class Sender(models.Model):
    wann = models.DateTimeField(auto_now_add=True); 
    von = models.EmailField();
    grund = models.CharField(max_length=95);
    nachricht = models.TextField();
    def __str__(self):
        speichern = self.wann.strftime('%Y/%b/%d;%H:%M:%S')+ ";" + self.von + ";" + self.grund
        return speichern
        

        
        
 