from django.conf.urls.defaults import *

urlpatterns = patterns('boxoffice.views',
    url(r'^$', 'show_registration_table'),
    url(r'^register/$', 'start_registration', name='start_ticket_registration'),
    url(r'^complete/$', 'complete_registration', name='complete_ticket_registration'),
)
