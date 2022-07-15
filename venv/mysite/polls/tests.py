import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1) # time은 현재 시간에서 1일 1초 전 시간 (음수)
        old_question= Question(pub_date=time)

        # self.assertIs(테스트 하고픈 조건, 기대하는 Boolean값)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
         was_published_recently() returns True for questions whose pub_date
         is within the last day.
        """

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59) # time은 현재 시간에서 23시간 59분 59초 전 시간 (양수)
        recent_question = Question(pub_date=time)

        self.assertIs(recent_question.was_published_recently(), True)

