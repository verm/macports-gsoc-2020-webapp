from django.test import TransactionTestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient

from ports.tests import setup
from ports.maintainer.models import Maintainer
from ports.port.models import Port


class TestURLsMaintainers(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.client = Client()
        setup.setup_test_data()

    def test_maintainer_url(self):
        response = self.client.get(reverse('maintainer', kwargs={
            'm': 'user'
        }))

        self.assertRedirects(response, '/search/?selected_facets=maintainers_exact:user')

    def test_old_url_redirect(self):
        response = self.client.get(reverse('maintainer_old', kwargs={
            'm': 'user'
        }))

        self.assertRedirects(response, reverse('maintainer', kwargs={
            'm': 'user'
        }), status_code=302, target_status_code=302)


class TestMaintainerAPIViews(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.client = APIClient()
        setup.setup_test_data()

    def test_list_view(self):
        response = self.client.get(reverse('maintainer-list'), format='json')
        data = response.data

        self.assertEquals(len(data['results']), 6)

        for m in data['results']:
            if m['github'] == 'user' and m['name'] == 'user':
                self.assertEquals(m['ports_count'], 2)

            if m['github'] == 'user' and m['name'] == 'user2':
                self.assertEquals(m['ports_count'], 1)

    def test_list_view_filter(self):
        response = self.client.get(reverse('maintainer-list'), {'github': 'user'}, format='json')
        data = response.data['results']

        self.assertEquals(len(data), 3)

    def test_detail_view(self):
        response = self.client.get(reverse('maintainer-detail', kwargs={'github': 'user2'}), format='json')
        data = response.data

        self.assertEquals(len(data), 1)

        response2 = self.client.get(reverse('maintainer-detail', kwargs={'github': 'user'}), format='json')
        data2 = response2.data

        self.assertEquals(len(data2), 3)


class TestMaintainerLoadAndUpdate(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.client = Client()
        setup.setup_test_data()

    def test_add_new_maintainer(self):
        # add another maintainer to the same port
        Port.add_or_update([{
            "portdir": "categoryA/port-A1",
            "name": "port-A1",
            "version": "1.2",
            "maintainers": [
                {
                    "email": {
                        "domain": "email.com",
                        "name": "user"
                    },
                    "github": "user"
                },
                {
                    "github": "user2"
                }
            ]
        }])

        self.assertEquals(Port.objects.get(name="port-A1").maintainers.all().count(), 2)
        self.assertEquals(Maintainer.objects.all().count(), 7)

        # Now remove the maintainer, this should not delete the object from Maintainer model,
        # and should only delete the relation
        Port.add_or_update([{
            "portdir": "categoryA/port-A1",
            "name": "port-A1",
            "version": "1.2",
            "maintainers": [
                {
                    "email": {
                        "domain": "email.com",
                        "name": "user"
                    },
                    "github": "user"
                }
            ]
        }])

        self.assertEquals(Port.objects.get(name="port-A1").maintainers.all().count(), 1)
        self.assertEquals(Maintainer.objects.all().count(), 7)

    def test_invalid_addition(self):
        Port.add_or_update([{
            "portdir": "categoryA/port-A1",
            "name": "port-A1",
            "version": "1.2",
            "maintainers": [
                {
                    "email": {
                        "domain": "email.com",
                        "name": "user"
                    },
                    "github": "user"
                },
                {
                    "email": {
                        "domain": "email.com",
                        "name": "user"
                    },
                    "github": "user"
                }
            ]
        }])

        self.assertEquals(Port.objects.get(name="port-A1").maintainers.all().count(), 1)
        self.assertEquals(Maintainer.objects.all().count(), 6)

    def test_existing_maintainer(self):
        # adding a maintainer that already exists to another port
        Port.add_or_update([{
            "portdir": "categoryA\/port-C1",
            "name": "port-A1",
            "version": "1.2.3",
            "maintainers": [
                {
                    "email": {
                        "domain": "macports.org",
                        "name": "user3"
                    },
                    "github": "user3"
                },
                {
                    "email": {
                        "domain": "email.com",
                        "name": "user"
                    },
                    "github": "user"
                }
            ]
        }])

        self.assertEquals(Port.objects.get(name="port-A1").maintainers.all().count(), 2)
        self.assertEquals(Maintainer.objects.all().count(), 6)

    def test_remove_maintainer(self):
        # adding a maintainer that already exists to another port
        Port.add_or_update([{
            "portdir": "categoryA\/port-C1",
            "name": "port-A1",
            "version": "1.2.3",
        }])

        self.assertEquals(Port.objects.get(name="port-A1").maintainers.all().count(), 0)
        self.assertEquals(Maintainer.objects.all().count(), 6)

