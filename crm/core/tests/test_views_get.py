from crm.core.tests.utils import BaseTestCase, send_get_request


class MyselfGetTest(BaseTestCase):
    def test_get_myself(self):
        endpoint = '/api/myself/'

        response = send_get_request(self.client, endpoint)
        assert response.status_code == 200, (response.status_code, response.content)

        response_json = response.json()
        assert response_json == []
