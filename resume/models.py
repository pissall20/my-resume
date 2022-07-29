from django.db import models

# Create your models here.


class Skill(models.Model):
    skill = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.skill


class Education(models.Model):
    course = models.CharField(max_length=120)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4, null=True, default="Present")
    school = models.CharField(max_length=120)
    writeup = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.course


class Experience(models.Model):
    designation = models.CharField(max_length=100)
    workplace = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_year = models.CharField(max_length=12)
    end_year = models.CharField(max_length=12, null=True, default="Present")
    experience_ul = models.TextField(max_length=1000)

    def __str__(self):
        return self.workplace


class Service(models.Model):
    heading_text = models.CharField(max_length=200)
    description_text = models.TextField(max_length=2000)
    order = models.IntegerField(null=True)
    icon_img = models.ImageField(upload_to="service_icons/", blank=True, null=True)

    def __str__(self):
        return self.heading_text


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.email
