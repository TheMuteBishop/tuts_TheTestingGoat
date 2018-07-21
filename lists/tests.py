from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_math(self):
        # this test should fail
        self.assertIn(2+2 , 3)

