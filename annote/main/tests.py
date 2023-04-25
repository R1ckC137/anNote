from django.test import TestCase, Client
from django.urls import reverse
from .models import Annote
from .forms import WriteForm


class AnnoteTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('main:main')

    def test_create_annote(self):
        form_data = {'annote': 'Test anNote'}
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your anNote has been saved!')


        # проверяею, что записка создана в базе данных
        self.assertEqual(Annote.objects.count(), 1)
        self.assertEqual(Annote.annote, form_data['annote'])

        # проверяею, что сгенерирован ссылка на записку
        self.assertIsNotNone(Annote.link)

        #проверяею, что формы были очищены после отправки
        write_form = response.context['write_form']
        self.assertEqual(write_form['annote'].value(), '')