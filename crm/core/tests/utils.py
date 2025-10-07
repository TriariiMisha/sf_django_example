import json

from rest_framework.test import APITestCase

from crm.core.models import User


def send_post_request(client, endpoint, payload):
    return client.post(
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


def send_get_request(client, endpoint):
    return client.get(endpoint)


def send_delete_request(client, endpoint):
    return client.delete(endpoint)


def create_user(
    username,
    first_name,
    last_name,
    email='example@mail.ru',
    is_staff=True,
    is_active=True,
    is_superuser=False,
):
    user = User(
        is_superuser=is_superuser,
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_staff=is_staff,
        is_active=is_active,
    )
    user.save()

    return user


class BaseTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()

        _ = create_user('test', 'Тест', 'Тестович')
