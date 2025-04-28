from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import StickyNote

class StickyNoteTests(TestCase):
    
    def setUp(self):
        self.note = StickyNote.objects.create(title='Test Note', content='This is a test note.')

    def test_create_note(self):
        note = StickyNote.objects.get(title='Test Note')
        self.assertEqual(note.content, 'This is a test note.')

    def test_update_note(self):
        self.note.title = 'Updated Title'
        self.note.save()
        updated_note = StickyNote.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Updated Title')

    def test_delete_note(self):
        note_id = self.note.id
        self.note.delete()
        with self.assertRaises(StickyNote.DoesNotExist):
            StickyNote.objects.get(id=note_id)

    def test_note_string_representation(self):
        self.assertEqual(str(self.note), 'Test Note')
