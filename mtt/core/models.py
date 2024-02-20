from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.username)

    def __unicode__(self):
        return "%d: %s" % (str(self.username), str(self.username))
