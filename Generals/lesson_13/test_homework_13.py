import unittest
from homework_13 import log_event


class TestLogEvent(unittest.TestCase):

    def test_success(self):
        with self.assertLogs('log_event', level='INFO') as captured:
            log_event("Spektra", "success")  # ім'я користувача і статус 'success'

        self.assertIn('Login event - Username: Spektra, Status: success', captured.output[0])

    def test_expired(self):
        with self.assertLogs('log_event', level='WARNING') as captured:
            log_event("Dambldor", "expired")

        self.assertIn('Login event - Username: Dambldor, Status: expired', captured.output[0])

    def test_failure(self):
        with self.assertLogs('log_event', level='ERROR') as captured:
            log_event("Khranoa", "failed")

        self.assertIn('Login event - Username: Khranoa, Status: failed', captured.output[0])