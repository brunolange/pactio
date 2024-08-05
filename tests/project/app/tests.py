import json
from http import HTTPStatus

from django.test import Client, TestCase


class TestPactio(TestCase):
    def test_broken_pact(self):
        test_broken_pact(self.client)

    def test_maintained_pact(self):
        test_maintained_pact(self.client)


def test_broken_pact(client: Client):
    response = client.post(
        "/app/my_view",
        json.dumps({"a": 1}),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_maintained_pact(client: Client):
    data = {
        "a_str": "hello",
        "an_int": 42,
        "a_bool": True,
        "a_float": 3.14,
        "a_list_of_ints": [1, 1, 3, 5, 8, 13, 21],
    }
    response = client.post(
        "/app/my_view",
        json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == data
