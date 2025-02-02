from django.contrib import admin
from django.test import TestCase

from ..admin import TestInstanceAdmin
from ..models import TestInstance


class TestInstanceAdminTest(TestCase):
    def test_admin_should_be_registered(self):
        assert isinstance(admin.site._registry[TestInstance], TestInstanceAdmin)

    def test_admin_should_set_list_display(self):
        expected = ("testcase", "testrun", "assignee", "status")

        assert TestInstanceAdmin.list_display == expected

    def test_admin_should_set_search_fields(self):
        expected = ("assignee",)

        assert TestInstanceAdmin.search_fields == expected

    def test_admin_should_set_list_filter(self):
        expected = ("testrun",)

        assert TestInstanceAdmin.list_filter == expected
