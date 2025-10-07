from crm.core.tests.utils import BaseTestCase, send_get_request
from crm.internal.products.tests.utils import create_product


class ProductsGetTest(BaseTestCase):
    endpoint = '/api/products'

    def setUp(self):
        _ = create_product('Product 1')
        _ = create_product('Product 2')

    def test_get_products(self):
        response = send_get_request(self.client, self.endpoint)
        assert response.status_code == 200

        # in case request is successful
        response_json = response.json()
        names = {item['name'] for item in response_json}

        assert len(response_json) == 2
        assert names == {'Product 1', 'Product 2'}


class ProductGetTest(BaseTestCase):
    base_url = '/api/products'

    def setUp(self):
        product = create_product('Product 1')
        product2 = create_product('Product 2')

        self.product_id = str(product.id)
        self.product2_id = str(product2.id)

    def test_get_product(self):
        endpoint = f'{self.base_url}/{self.product_id}'

        response = send_get_request(self.client, endpoint)
        assert response.status_code == 200

        # in case request is successful
        response_json = response.json()

        assert response_json['name'] == 'Product 1'

    def test_get_another_product(self):
        endpoint = f'{self.base_url}/{self.product2_id}'

        response = send_get_request(self.client, endpoint)
        assert response.status_code == 200

        # in case request is successful
        response_json = response.json()

        assert response_json['name'] == 'Product 2'

    def test_get_product_with_invalid_id(self):
        endpoint = f'{self.base_url}/12345678'

        response = send_get_request(self.client, endpoint)
        assert response.status_code == 400

    def test_get_product_not_exist(self):
        endpoint = f'{self.base_url}/1c403528-b613-4f12-a3b4-d11bc03a3ee6'

        response = send_get_request(self.client, endpoint)
        assert response.status_code == 404
