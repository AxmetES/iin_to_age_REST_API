import datetime
from datetime import date

from rest_framework.viewsets import ModelViewSet

# Create your views here.
from iin_to_age.models import Person
from iin_to_age.serializers import PersonSerializer


class PersonViewSetApi(ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        iin = self.request.query_params.get('iin', None)
        if iin:
            queryset = queryset.filter(iin=iin)
        return queryset

    def perform_create(self, serializer):
        century = self.request.data.get('iin')[6]
        print(century)
        iin_date = self.request.data.get('iin')[0:6]
        if century in '34':
            iin_date = '19' + iin_date
        elif century in '56':
            iin_date = '20' + iin_date
        today = date.today()
        born = datetime.datetime.strptime(iin_date, '%Y%m%d').date()
        age = (((born - today).days) / 365) * - 1
        serializer.save(age=age)
