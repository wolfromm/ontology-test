from my_app import app, init_onto
from unittest import TestCase


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.onto = init_onto()

    def test_add_concept_w_valid_classname_and_superclassname(self):
        classname = "RetailBank"
        superclassname = "Bank"

        assert self.onto[classname] is None
        assert self.onto[superclassname] is not None

        res = self.app.post('/companyontology/concepts',
                            data=dict(classname=classname,
                                      superclassname=superclassname))

        assert self.onto[classname] is not None
        assert self.onto[superclassname] is not None
        assert res.status_code == 201   # HTTP code for "created"

