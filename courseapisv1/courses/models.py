from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_data = models.DateTimeField(auto_now_add=True, null=True)
    updated_data = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True
        ordering = ['-id']

class Course(models.Model):
    subject = models.CharField(max_length=255,null=False)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/%Y/%m")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ['subject', 'category']

class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to="lessons/%Y/%m")
    course = models.ForeignKey(Course,on_delete=models.RESTRICT)

    def __str__(self):
        return self.subject

