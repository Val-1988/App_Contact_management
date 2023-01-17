import django_filters

from .models import *


class ContactFilter(django_filters.FilterSet):

    class Meta:
        model = Contact
        fields = "__all__"
