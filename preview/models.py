from django.db import models
from django.utils import timezone
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import sys


# Create your models here.
def get_uplaod_file_name(image, filename):
    return u'photos/%s_%s' % (str(image.name), filename)

def get_uplaod_file_doc_name(image, filename):
    return u'person/%s_%s' % (str(image.firstName), filename)


class School(models.Model):
    term_name = models.CharField(max_length=30)
    name = models.CharField(max_length=200)


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=300)

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=False, null=False)
    query = models.TextField(blank=False, null=False)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="add Item image",
                              upload_to=get_uplaod_file_name)

    def __str__(self):
        return self.query

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('contact-detail', args=[str(self.id)])

class Personnel(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(default="Add Image", upload_to=get_uplaod_file_doc_name)
    document = models.FileField(default="Add Document", upload_to=get_uplaod_file_doc_name)
    video = models.FileField(default="Add Video File", upload_to=get_uplaod_file_doc_name)

    def __str__(self):
        return self.query

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('person-detail', args=[str(self.id)])