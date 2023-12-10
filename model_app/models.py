from django.db import models

# Create your models here.

class contactModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    email_field = models.EmailField()
    integer_field = models.IntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()

    def __str__(self):
        return self.email_field
