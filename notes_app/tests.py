from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from models import Note, Book, BookContent


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

    def test_add_note(self):
        # test filling form - added to db
        # test published_date is added
        # test non valid databases
        # test redirect to created page
        response1 = self.client.get(reverse('add_note'))

        self.assertEqual(response1.status_code, 200)

        response2 = self.client.post(reverse('add_note'), {'title': 'new_title',
                                                           'text': 'new_text_xxxxxxx'})
        last_note = Note.objects.all().last()
        # print Note.objects.all().get(id=2).published_date
        self.assertEqual(last_note.title, 'new_title'.upper())
        self.assertEqual(last_note.text, 'new_text_xxxxxxx')
        self.assertIsNotNone(last_note.published_date)
        self.assertEqual(self.client.get(
            reverse('note_detail', kwargs={'pk': last_note.pk})).status_code, 200)

        # note was not added to DB, len(text) is not validate
        response3 = self.client.post(reverse('add_note'), {'title': 'new_title2',
                                                           'text': 'new_text'})
        last_note = Note.objects.all().last()
        self.assertNotEqual(last_note.title, 'new_title2')

    def test_upper_case_custom_field(self):
        response = self.client.post(reverse('add_note'), {'title': 'new_title',
                                                          'text': 'new_text_xxxxxxx'})
        last_note = Note.objects.all().last()
        self.assertEqual(last_note.title, 'new_title'.upper())

    def test_number_of_notes(self):
        # current number of notes
        cur_notes_num = len(Note.objects.all())

        # checking on different pages
        response = self.client.get(self.home_url)
        response2 = self.client.get(reverse('add_note'))
        response3 = self.client.get(reverse('note_detail', kwargs={'pk': 1}))
        self.assertContains(response, '<span id="noteNumber" class="badge">' +
                            str(cur_notes_num) + '</span>', html=True)
        self.assertContains(response2, '<span id="noteNumber" class="badge">' +
                            str(cur_notes_num) + '</span>', html=True)
        self.assertContains(response3, '<span id="noteNumber" class="badge">' +
                            str(cur_notes_num) + '</span>', html=True)

        # if new note is added
        response4 = self.client.post(
            reverse('add_note'), {'title': 'new_title', 'text': 'new_text_xxxxxxx'})
        add_to_notes_num = len(Note.objects.all())
        self.assertEqual(cur_notes_num + 1, add_to_notes_num)

        # if DB is empty
        Note.objects.all().delete()
        del_to_notes_num = len(Note.objects.all())
        self.assertEqual(del_to_notes_num, 0)

    def test_add_note_ajax(self):
        # test filling form - added to db
        # test published_date is added
        # test non valid databases
        # test redirect to created page
        # test is_ajax
        response1 = self.client.get(reverse('add_note'))

        self.assertEqual(response1.status_code, 200)

        response2 = self.client.post(reverse('add_note'), {'title': 'new_title',
                                                           'text': 'new_text_xxxxxxx'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        last_note = Note.objects.all().last()
        # AJAX redirected successfully
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(last_note.title, 'new_title'.upper())
        self.assertEqual(last_note.text, 'new_text_xxxxxxx')
        self.assertIsNotNone(last_note.published_date)
        self.assertEqual(self.client.get(
            reverse('note_detail', kwargs={'pk': last_note.pk})).status_code, 200)

        # note was not added to DB, len(text) is not validate
        response3 = self.client.post(reverse('add_note'), {'title': 'new_title2',
                                                           'text': 'new_text'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        last_note = Note.objects.all().last()
        # AJAX stayed on the same page
        self.assertEqual(response3.status_code, 200)
        self.assertNotEqual(last_note.title, 'new_title2')

    def test_add_note_ajax_image(self):
        # test filling form - added to db
        # test published_date is added
        # test non valid databases
        # test redirect to created page
        # test is_ajax
        response1 = self.client.get(reverse('add_note'))

        self.assertEqual(response1.status_code, 200)

        response2 = self.client.post(reverse('add_note'), {'title': 'new_title',
                                                           'text': 'new_text_xxxxxxx'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        last_note = Note.objects.all().last()
        # AJAX redirected successfully
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(last_note.title, 'new_title'.upper())
        self.assertEqual(last_note.text, 'new_text_xxxxxxx')
        self.assertIsNotNone(last_note.published_date)
        self.assertEqual(self.client.get(
            reverse('note_detail', kwargs={'pk': last_note.pk})).status_code, 200)
        # no photo
        self.assertFalse(bool(last_note.photo))

        # ther is photo
        note_pk1 = Note.objects.get(pk=1)
        self.assertTrue(bool(note_pk1.photo))

    def test_book_to_notes_many_to_many(self):

        note1 = Note.objects.create(title='new_title',
                                    text='new_text_xxxxxxx')
        book1 = Book.objects.create(title='ABC')

        BookContent.objects.create(note=note1, book=book1)

        # check if BookContent is non empty
        book_content1 = BookContent.objects.last()
        self.assertIn('new_title', unicode(book_content1))
        self.assertIn('ABC', unicode(book_content1))

        # check if book is deleted when it is empty
        num_books = len(Book.objects.all())
        note1.delete()
        self.assertEqual(num_books - 1, len(Book.objects.all()))
        

from channels import Group
from channels.test import ChannelTestCase

class AsynTest(ChannelTestCase):

    def test_try(self):
        Group('test_group').add(u'test_channel')
        Group('test_group').send({"value": 999})
        result = self.get_next_message(u'test_channel', require=True)
        self.assertEqual(result['value'],999)
        
        