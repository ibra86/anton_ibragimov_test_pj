from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# Create your tests here.


class TestNoteList(TestCase):

    fixtures = ['fixture_data.json']

    def setUp(self):

        self.client = Client()
        self.home_url = reverse('home')

    def test_notes_list(self):
        response = self.client.get(self.home_url)

        # checking response status
        self.assertEqual(response.status_code, 200)

        # checking content
        self.assertIn('lorem ipsum'.lower(), response.content.lower())
        self.assertIn('consectetur adipiscing elit', response.content)
        self.assertIn('published', response.content)

    def test_link_to_detail_note(self):
        response = self.client.get(reverse('note_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

        # checking content
        self.assertIn('lorem ipsum'.lower(), response.content.lower())
        self.assertIn('consectetur adipiscing elit', response.content)
        self.assertIn('2017', response.content)
