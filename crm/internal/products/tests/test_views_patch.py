from crm.core.tests.utils import BaseTestCase, send_patch_request
from crm.internal.products.tests.utils import create_product


class ProductPatchTest(BaseTestCase):
    base_url = '/api/products'

    def setUp(self):
        product = create_product('Product 1')

        self.product_id = str(product.id)

    def test_patch_product(self):
        payload = {
            'isActive': False,
            'name': 'Another Name',
        }
        endpoint = f'{self.base_url}/{self.product_id}'

        response = send_patch_request(self.client, endpoint, payload)
        assert response.status_code == 200

        # in case request is successful
        response_json = response.json()

        assert not response_json['isActive']
        assert response_json['name'] != 'Another Name'

    def test_patch_product_with_invalid_id(self):
        payload = {
            'isActive': False,
            'name': 'Another Name',
        }
        endpoint = f'{self.base_url}/12345678'

        response = send_patch_request(self.client, endpoint, payload)
        assert response.status_code == 400

    def test_patch_product_not_exist(self):
        payload = {
            'isActive': False,
            'name': 'Another Name',
        }
        endpoint = f'{self.base_url}/1c403528-b613-4f12-a3b4-d11bc03a3ee6'

        response = send_patch_request(self.client, endpoint, payload)
        assert response.status_code == 404

    def test_create_product_bad_input_data(self):
        endpoint = f'{self.base_url}/{self.product_id}'
        payload = {'isActive': 1234}

        response = send_patch_request(self.client, endpoint, payload)
        assert response.status_code == 400
