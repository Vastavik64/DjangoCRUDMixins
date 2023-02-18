from django.db import models

# Create your models here.
class user(models.Model):
    '''
    This class creates a model user in django database with the fields defined
    '''
    id = models.AutoField(primary_key = True, auto_created=True)
    name = models.TextField()
    birthdate = models.DateField()
    gender = models.TextField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name            #This method defines an instance of a class which is displayed as a string