from django.test import TestCase
from sendmail.views import send_email


class SendEmailTests(TestCase):

    def test_send_email_succeed_with_one(self):
        """
        send_email() function returns the sent emails count
        """
        count = send_email('sunmoon11@yandex.ru', 'This text is from test_send_email_succeed().')
        self.assertIs(count, 1)
