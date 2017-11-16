from django.db import models

from account.models import Account
from dashboard.models import Dashboard
from tag.models import Tag

# Create your models here.
class Project(models.Model):
    client = models.ForeignKey(
        Account,
        on_delete = models.CASCADE,
        blank = False)

    dashboard = models.ForeignKey(
        Dashboard,
        on_delete = models.CASCADE,
        blank = True)   # Belongs to a freelancer once they accept an offer

    title = models.CharField(
        max_length = 50,
        blank = False)

    description = models.TextField(
        blank = False)

    tags = models.ManyToManyField(
        Tag,
        blank = True)

    is_taken = models.BooleanField(
        default = False,
        blank = False)

    def __str__(self):
        return self.title

class Compensation(models.Model):
    currency = models.CharField(
        max_length = 3,
        blank = False)

    value = models.PositiveIntegerField(
        default = 0,
        blank = False)

    project = models.OneToOneField(
        Project,
        on_delete = models.CASCADE,
        blank = False)

    def __str__(self):
        return "{0} {1}".format(self.currency, self.value)

class Task(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE,
        blank = False)

    name = models.TextField(
        max_length = 50,
        blank = False)

    description = models.TextField(
        blank = False)

    is_complete = models.BooleanField(
        default = False,
        null = False,
        blank = False)

    def __str__(self):
        return self.name
