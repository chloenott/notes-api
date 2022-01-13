from django.test import TestCase
from django.contrib.auth import get_user, get_user_model

# Create your tests here.
from .models import Note
class NoteTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        testuser = get_user_model().objects.create_user(
            username='chloe', email='chloe@nott.email', password='pass'
        )
        testuser.save()

        test_note = Note.objects.create(
            headline = 'Note title',
            topic = 'Test',
            details = 'Hi Chloe in the future!',
            user = testuser
        )
        test_note.save()

    def test_get(self):
        response = Note.objects.get(id=1)
        assert str(response.headline) == 'Note title'
        assert str(response.topic) == 'Test'
        assert str(response.details) == 'Hi Chloe in the future!'

    def test_put(self):
        Note.objects.update(headline='Updated title', id=1)
        response = Note.objects.get(id=1)
        assert str(response.headline) == 'Updated title'
        assert str(response.user.username) == 'chloe'

    # TODO: Not required for assignment. Tests for note delete, cascade on user delete, that datetime_create and datetime_update work properly, and that users can't modify other user's notes.
