import json
from http import HTTPStatus

from django.test import Client, TestCase, modify_settings


class TestPactioMiddleware(TestCase):
    def test_broken_pact(self):
        test_broken_pact(self.client)

    def test_maintained_pact_with_json(self):
        test_maintained_pact_with_json(self.client)

    def test_maintained_pact_with_form(self):
        test_maintained_pact_with_form(self.client)


def test_broken_pact(client: Client):
    response = client.post(
        "/app/echo",
        json.dumps({"a": 1}),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response = client.post(
        "/app/echo",
        "this is clearly not json",
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_maintained_pact_with_form(client: Client):
    data = {
        "a_str": "hello",
        "an_int": 42,
        "a_bool": True,
        "a_float": 3.14,
        "a_list_of_ints": [1, 1, 3, 5, 8, 13, 21],
    }
    response = client.post("/app/echo", data=data)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == data


def test_maintained_pact_with_json(client: Client):
    data = {
        "a_str": "hello",
        "an_int": 42,
        "a_bool": True,
        "a_float": 3.14,
        "a_list_of_ints": [1, 1, 3, 5, 8, 13, 21],
    }
    response = client.post(
        "/app/echo",
        json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == data


@modify_settings(
    MIDDLEWARE={
        "remove": "pactio.middleware.PactioMiddleware",
    }
)
class TestPactioDecorator(TestCase):
    # def test_broken_pact_with_decorator(self):
    #     test_broken_pact_with_decorator(self.client)

    def test_maintained_pact_with_decorator(self):
        test_maintained_pact_with_decorator(self.client)


def test_broken_pact_with_decorator(client: Client):
    response = client.post(
        "/app/decorated_echo",
        json.dumps({"a": 1}),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_maintained_pact_with_decorator(client: Client):
    data = {
        "a_str": "hello",
        "an_int": 42,
        "a_bool": True,
        "a_float": 3.14,
        "a_list_of_ints": [1, 1, 3, 5, 8, 13, 21],
    }
    response = client.post(
        "/app/decorated_echo",
        json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == data
