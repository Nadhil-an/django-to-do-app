from django.db import models

# Create your models here.
class Todo(models.Model):
    srno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    user=models.CharField(max_length=200)

    def __str__(self):
        return self.title
