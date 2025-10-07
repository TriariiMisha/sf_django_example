from crm.core.tests.utils import BaseTestCase, send_post_request


class ProductCreateTest(BaseTestCase):
    endpoint = '/api/products'

    def test_create_product(self):
        payload = {'name': 'Классный Продукт'}

        response = send_post_request(self.client, self.endpoint, payload)
        assert response.status_code == 201

        # in case request is successful
        response_json = response.json()

        assert payload['name'] == response_json['name']
        assert 'id' in response_json

    def test_create_product_bad_input_data(self):
        payload = {'name': True}

        response = send_post_request(self.client, self.endpoint, payload)
        assert response.status_code == 400
