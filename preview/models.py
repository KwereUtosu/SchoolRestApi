from django.db import models
from django.utils import timezone
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import sys


# Create your models here.
def get_uplaod_file_name(image, filename):
    return u'photos/%s/%s_%s' % (str(image.name),
                                 str(timezone.now()).replace('.', '_'),
                                 filename)


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

    # def save(self):
    #     im = Image.open(self.image)
    #     output = BytesIO()
    #     im = im.resize((500, 500))
    #
    #     im.save(output, format='PNG', optimize=True, quality=95)
    #     output.seek(0)
    #
    #     self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.image.name.split('.')[0], 'image/jpeg',
    #                                       sys.getsizeof(output), None)
    #
    #     self.save()

        # super(self).save()

    def __str__(self):
        return self.query