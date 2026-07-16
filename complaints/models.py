from django.db import models
class Complaint(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Solved', 'Solved'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    complaint_type = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.name}"

# Create your models here.
