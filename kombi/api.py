""" Main application API written in Restless with Django """

from datetime import datetime
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from kombi.models import Delivery

class DeliveryResource(DjangoResource):
    """ Prepares the Delivery Model as API Resource """
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'title': 'title',
        'freighter': 'freighter',
        'departure': 'departure',
        'arrival': 'arrival',
        'deadline': 'deadline',
        'volume': 'volume',
        'weight': 'weight',
        'description': 'description'
    })
    def is_authenticated(self):
        """ Verifies authorization of modification of API objects """
        # Open everything wide!
        # DANGEROUS, DO NOT DO IN PRODUCTION.
        return True

        # An OAuth provider will be integrated.

        # Alternatively, if the user is logged into the site...
        # return self.request.user.is_authenticated()

        # Alternatively, you could check an API key. (Need a model for this...)
        # from myapp.models import ApiKey
        # try:
        #     key = ApiKey.objects.get(key=self.request.GET.get('api_key'))
        #     return True
        # except ApiKey.DoesNotExist:
        #     return False

    def serialize_list(self, data):
        if data is None:
            return ''
        # Check for a ``Data``-like object. We should assume ``True`` (all
        # data gets prepared) unless it's explicitly marked as not.
        if not getattr(data, 'should_prepare', True):
            formatted = data.value
        else:
            formatted = [self.prepare(item) for item in data]
        return self.serializer.serialize(formatted)

    # GET /kombi/deliveries/
    def list(self):
        """ Lists all delivery intances """
        return Delivery.objects.all()

    # GET /kombi/deliveries/<pk>/
    def detail(self, pk, **kwargs):
        """ Lists one specific delivery intances """
        return Delivery.objects.get(id=pk)

    # POST /kombi/deliveries/
    def create(self):
        return Delivery.objects.create(
            title=self.data['title'],
            freighter=int(self.data['freighter']),
            departure=self.data['departure'],
            arrival=self.data['arrival'],
            deadline=datetime.strptime(self.data['deadline'], '%d-%m-%Y %H:%M'),
            volume=float(self.data['volume']),
            weight=float(self.data['weight']),
            description=self.data['description']
        )

    # PUT /kombi/deliveries/<pk>/
    def update(self, pk, **kwargs):
        try:
            delivery = Delivery.objects.get(id=pk)
        except Delivery.DoesNotExist:
            delivery = Delivery()
        delivery.title = self.data['title'],
        delivery.freighter = int(self.data['freighter'])
        delivery.departure = self.data['departure']
        delivery.arrival = self.data['arrival']
        delivery.deadline = datetime.strptime(self.data['deadline'], '%d-%m-%Y %H:%M')
        delivery.volume = float(self.data['volume'])
        delivery.weight = float(self.data['weight'])
        delivery.description = self.data['description']
        delivery.save()
        return delivery

    # DELETE /kombi/deliveries/<pk>/
    def delete(self, pk, **kwargs):
        Delivery.objects.get(id=pk).delete()
