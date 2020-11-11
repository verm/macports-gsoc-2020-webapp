from django.shortcuts import HttpResponseRedirect, reverse
from rest_framework import viewsets, filters, mixins
from rest_framework.response import Response
import django_filters

from ports.maintainer.models import Maintainer
from ports.maintainer.forms import MaintainerAutocompleteForm
from ports.maintainer.serializers import MaintainerListSerializer, MaintainerDetailSerializer, MaintainerHaystackSerializer


def maintainer(request, m):
    return HttpResponseRedirect("{}?selected_facets=maintainers_exact:{}".format(reverse('search'), m))


# VIEWS FOR DJANGO REST FRAMEWORK


class MaintainerAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MaintainerListSerializer
    queryset = Maintainer.objects.all()
    lookup_field = 'github'
    lookup_value_regex = '[a-zA-Z0-9_.-]+'
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'github']
    filterset_fields = ['name', 'github']

    def retrieve(self, request, *args, **kwargs):
        # Due to inconsistencies in name - domain - GitHub combinations used by maintainer's
        # in PortFiles, multiple objects might be returned when searching for a maintainer by
        # their GitHub id. Hence, we return a list instead of a single object.
        queryset = Maintainer.objects.filter(github=kwargs['github'])
        result = MaintainerDetailSerializer(queryset, many=True)
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
