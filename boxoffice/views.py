import uuid
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.forms.models import modelformset_factory
from models import Ticket,TicketGroup

TicketFormSet = modelformset_factory(Ticket, extra=0)

def show_registration_table(request):
    return render_to_response('boxoffice/ticketgroup_table.html',
                              {'ticket_groups': TicketGroup.objects.all()})


@require_POST
def start_registration(request):

    # get form data
    group_id = int(request.POST['group_id'])
    num_tickets = int(request.POST.get('tickets', 1))

    group = get_object_or_404(TicketGroup, pk=group_id)

    # validate num_tickets
    if num_tickets > group.max_tickets or num_tickets < group.min_tickets:
        return HttpResponseBadRequest('Number of tickets requested must be between %s and %s' % (group.min_tickets, group.max_tickets))
    if group.registrations.count() + num_tickets > group.quantity:
        return HttpResponseBadRequest('Cannot fulfilly request, only %s tickets remain' % (group.quantity - group.registrations.count()))

    # generate a new UUID and create the appropriate registrations
    new_uuid = uuid.uuid4().hex
    for x in xrange(num_tickets):
        group.registrations.create(uuid=new_uuid)

    formset = TicketFormSet(queryset=Ticket.objects.filter(uuid=new_uuid))

    return render_to_response('boxoffice/register.html', {'formset':formset,
                                                          'uuid':new_uuid})

@require_POST
def complete_registration(request):

    # get form data
    new_uuid = request.POST['uuid']
    formset = TicketFormSet(request.POST, queryset=Ticket.objects.filter(uuid=new_uuid))

    # save tickets if form is valid
    if formset.is_valid():
        tickets = []
        for form in formset.forms:
            ticket = form.save(commit=False)
            ticket.active = True
            ticket.save()
            tickets.append(ticket)
        return render_to_response('boxoffice/registration_complete.html', 
                                  {'tickets':tickets, 'ticket_group':tickets[0].group})

    # show form again if validation failed
    return render_to_response('boxoffice/register.html', {'formset':formset,
                                                          'uuid':new_uuid})
