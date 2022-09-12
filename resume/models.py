from django.db import models
from django.utils.text import slugify
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
    location = models.CharField(max_length=100)
    writeup = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.course


class Experience(models.Model):
    designation = models.CharField(max_length=100)
    workplace = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_year = models.CharField(max_length=12)
    end_year = models.CharField(max_length=12, null=True, default="Present")
    experience_ul = models.TextField(max_length=2000)

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


class ProjectCategory(models.Model):
    name = models.CharField(max_length=200, default="Websites")
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProjectCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField(max_length=2000, blank=True, null=True, default="#")

    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, default="Others")
    project_desc = models.TextField(max_length=5000, null=True)
    date = models.DateField(null=True, auto_now_add=True)
    client = models.CharField(max_length=200, null=True, blank=True)
    order = models.IntegerField(default=999)
    # Images
    image1 = models.ImageField(upload_to="project_img/", blank=True, null=True)
    image2 = models.ImageField(upload_to="project_img/", blank=True, null=True)
    image3 = models.ImageField(upload_to="project_img/", blank=True, null=True)

    def __str__(self):
        return self.name


