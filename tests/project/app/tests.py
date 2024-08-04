import json
from http import HTTPStatus

from django.test import Client, TestCase


class TestPactio(TestCase):
    def test_simple_pact(self):
        test_simple_pact(self.client)


def test_simple_pact(client: Client):
    response = client.post("/app/my_view", json={"a": 1})
    assert response.status_code == HTTPStatus.OK
    assert json.loads(response.body) == {
        "a_str": "hello",
        "an_int": 42,
        "a_bool": True,
        "a_float": 3.14,
        "a_list_of_ints": [1, 1, 3, 5, 8, 13, 21],
    }
