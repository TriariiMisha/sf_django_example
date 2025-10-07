from crm.internal.products.models import Product


def create_product(name, created_by='test login'):
    product = Product(name=name, created_by=created_by)
    product.save()

    return product
