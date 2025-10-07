from crm.core.tests.utils import BaseTestCase, send_delete_request
from crm.internal.products.models import Product
from crm.internal.products.tests.utils import create_product


class ProductDeleteTest(BaseTestCase):
    base_url = '/api/products'

    def setUp(self):
        product = create_product('Product 1')

        self.product_id = str(product.id)

    def test_delete_product(self):
        endpoint = f'{self.base_url}/{self.product_id}'

        response = send_delete_request(self.client, endpoint)
        assert response.status_code == 204

        # in case request is successful
        assert Product.objects.count() == 0

    def test_delete_product_with_invalid_id(self):
        endpoint = f'{self.base_url}/12345678'

        response = send_delete_request(self.client, endpoint)
        assert response.status_code == 400

    def test_delete_product_not_exist(self):
        endpoint = f'{self.base_url}/1c403528-b613-4f12-a3b4-d11bc03a3ee6'

        response = send_delete_request(self.client, endpoint)
        assert response.status_code == 404
