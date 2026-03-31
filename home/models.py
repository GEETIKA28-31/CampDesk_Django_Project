from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    branch = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='students/', default='students/default.jpg')

    def __str__(self):
        return self.name
    
class SavedRequest(models.Model):   # CART
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Request(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    created_at = models.DateTimeField(auto_now_add=True)