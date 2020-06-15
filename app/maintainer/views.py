from django.shortcuts import HttpResponseRedirect, reverse
from rest_framework import viewsets, filters, mixins
from rest_framework.response import Response
import django_filters

from maintainer.models import Maintainer
from maintainer.forms import MaintainerAutocompleteForm
from maintainer.serializers import MaintainerListSerializer, MaintainerDetailSerializer, MaintainerHaystackSerializer


def maintainer(request, m):
    return HttpResponseRedirect("{}?selected_facets=maintainers_exact:{}".format(reverse('search'), m))


# VIEWS FOR DJANGO REST FRAMEWORK


class MaintainerView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MaintainerListSerializer
    queryset = Maintainer.objects.all()
    lookup_field = 'github'
    lookup_value_regex = '[a-zA-Z0-9_.]+'
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'domain', 'github']
    filterset_fields = ['name', 'domain', 'github']

    def retrieve(self, request, *args, **kwargs):
        result = MaintainerDetailSerializer(self.get_object())
        return Response(result.data)


class MaintainerAutocompleteView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MaintainerHaystackSerializer
    form = None
    form_class = MaintainerAutocompleteForm

    def build_form(self):
        data = self.request.GET
        return self.form_class(data, None)

    def get_queryset(self, *args, **kwargs):
        self.form = self.build_form()
        return self.form.search()
