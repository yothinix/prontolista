from django.db import models

from django_extensions.db.models import TimeStampedModel

from testcases.models import TestCase
from testruns.models import TestRun


class TestInstance(TimeStampedModel):
    testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    testrun = models.ForeignKey(TestRun, on_delete=models.CASCADE)
    assignee = models.CharField(null=True, blank=True, max_length=300)
    STATUSES = (("passed", "Passed"), ("blocked", "Blocked"), ("failed", "Failed"))
    status = models.CharField(null=True, blank=True, max_length=300, choices=STATUSES)
