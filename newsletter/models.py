from django.db import models

# Create your models here.


class SignUp(models.Model):

    # removed commas between fields - that was a type that I missed in the
    # last tutorial.

    # added default values or null=true to each because
    # makemigrations failed without it.  Newer version maybe?

    email = models.EmailField(default='user@domain.com')
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):  # Python 2.X uses __unicode__

        return self.email
