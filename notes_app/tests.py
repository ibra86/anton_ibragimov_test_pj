from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from models import Note


# Create your tests here.
		
class TestNoteList(TestCase):

	def setUp(self):
		note1, created = Note.objects.get_or_create(
			title='lorem ipsum',
			text='sadfasdfasdfasdf')
		
		self.client = Client()
		
		self.url = reverse('home')
	
	def test_notes_list(self):
		response = self.client.get(self.url)
		
		# checking response status
		self.assertEqual(response.status_code, 200)
		
		# checking content
		self.assertIn('lorem ipsum', response.content)
		self.assertIn('sadfasdfasdfasdf', response.content)
		self.assertIn('published', response.content)