from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from models import Note


# Create your tests here.

class TestNoteList(TestCase):

	fixtures = ['fixture_data.json']

	def setUp(self):
		# note1, created = Note.objects.get_or_create(
			# title='lorem ipsum',
			# text='sadfasdfasdfasdf')

		self.client = Client()
		self.url = reverse('home')

	def test_notes_list(self):
		response = self.client.get(self.url)

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

	def test_add_note(self):
		# test filling form - added to db
		# test published_date is added
		# test non valid databases
		# test redirect to created page
		response1 = self.client.get(reverse('add_note'))

		self.assertEqual(response1.status_code, 200)

		response2 = self.client.post(reverse('add_note'), {'title':'new_title',
			'text':'new_text_xxxxxxx'})
		last_note = Note.objects.all().last()
		# print Note.objects.all().get(id=2).published_date
		self.assertEqual(last_note.title,'new_title'.upper())
		self.assertEqual(last_note.text,'new_text_xxxxxxx')
		self.assertIsNotNone(last_note.published_date)
		self.assertEqual(self.client.get(reverse('note_detail', kwargs={'pk': last_note.pk})).status_code,200)

		# note was not added to DB, len(text) is not validate
		response3 = self.client.post(reverse('add_note'), {'title':'new_title2',
			'text':'new_text'})
		last_note = Note.objects.all().last()
		self.assertNotEqual(last_note.title,'new_title2')


	def test_upper_case_custom_field(self):
		response = self.client.post(reverse('add_note'), {'title':'new_title',
			'text':'new_text_xxxxxxx'})
		last_note = Note.objects.all().last()
		self.assertEqual(last_note.title,'new_title'.upper())
