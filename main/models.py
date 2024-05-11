from django.db import models

# Create your models here.
class Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    testname = models.CharField(max_length=255)
    testdescription = models.CharField(max_length=255)