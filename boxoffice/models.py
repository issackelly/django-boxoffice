from datetime import datetime
import time
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class TicketGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    quantity = models.IntegerField()
    min_tickets = models.IntegerField(default=1)
    max_tickets = models.IntegerField(default=4)

    def __unicode__(self):
        return self.name

    def registration_open(self):
        return self.start_date < datetime.now() < self.end_date
    registration_open.boolean = True

    def seats_left(self):
        return max(self.quantity - self.registrations.count(), 0)

    def get_quantity_options(self):
        return range(self.min_tickets, min(self.seats_left(), self.max_tickets)+1) or [0]

BOXOFFICE_HOLD_MINUTES = getattr(settings, 'BOXOFFICE_HOLD_MINUTES', 30)

class TicketManager(models.Manager):
    def unclaimed(self):
        cutoff = datetime.fromtimestamp(time.time()-(BOXOFFICE_HOLD_MINUTES*60))
        return self.filter(active=False, registration_date__lt=cutoff)

class Ticket(models.Model):
    group = models.ForeignKey(TicketGroup, related_name='registrations', editable=False)
    uuid = models.CharField(max_length=32, editable=False)
    registration_date = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField(default=False, editable=False)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField()
    organization = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    other = models.TextField('Who are you/what do you do?', blank=True)

    objects = TicketManager()

    def __unicode__(self):
        return '%s %s for %s' % (self.first_name, self.last_name, self.group)
