import json

from rest_framework.test import APITestCase


def send_post_request(client, endpoint, payload):
    return client.post(
        endpoint,
        json.dumps(payload),
        content_type='application/json',
    )


def send_put_request(client, endpoint, payload):
    return client.put(
        endpoint,
        json.dumps(payload),
        content_type='application/json',
    )


def send_patch_request(client, endpoint, payload):
    return client.patch(
        endpoint,
        json.dumps(payload),
        content_type='application/json',
    )


def send_delete_request(client, endpoint):
    return client.delete(endpoint)


def send_get_request(client, endpoint):
    return client.get(endpoint)


class BaseTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()
