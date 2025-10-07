from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from crm.core.serializers import ErrorResponseSerializer
from crm.internal.products.models import Product
from crm.internal.products.payload_serializers import (
    ProductCreatePayloadSerializer,
    ProductUpdatePayloadSerializer,
)
from crm.internal.products.representations import ProductRepresentation
from crm.internal.products.response_serializers import ProductDtoSerializer
from crm.utils.errors import (
    BadRequestException,
    ResourceNotFoundException,
    SerializationException,
)
from crm.utils.validators import is_valid_uuid


class ProductsGetCreate(APIView):
    serializer_post_request = ProductCreatePayloadSerializer  # тело запроса на создание (с какими параметрами)
    serializer_post_response = (
        ProductDtoSerializer  # то, что отдается после создания объекта (инфа про новый)
    )

    serializer_get_response = ProductDtoSerializer

    @extend_schema(
        request=serializer_post_request(),
        responses={
            201: serializer_post_response(),  # то, что отдается после создания объекта
            400: ErrorResponseSerializer(),
            404: ErrorResponseSerializer(),
        },
        tags=['Products'],
        summary='Создать новый продукт',
        operation_id='product_create',
    )
    def post(self, request):
        # validate request data
        serializer = self.serializer_post_request(data=request.data)

        if not serializer.is_valid():
            raise BadRequestException(str(serializer.errors))

        # parse request data
        request_username = (
            request.user.username if request.user.username else 'test_user'
        )
        request_data = serializer.data

        name = request_data['name']

        # create new object
        product = Product(
            name=name,
            created_by=request_username,
        )
        product.save()

        # prepare response dto
        product_dto = ProductRepresentation().get_dto(product)

        # validate response dto
        serializer = self.serializer_post_response(data=product_dto)
        if not serializer.is_valid():
            raise SerializationException(
                f'ProductDto serialization error: {serializer.errors}'
            )

        return Response(serializer.data, status=201)

    @extend_schema(
        responses={
            200: serializer_get_response(many=True),
            400: ErrorResponseSerializer(),
            404: ErrorResponseSerializer(),
        },
        tags=['Products'],
        summary='Получить информацию по всем продуктам',
        operation_id='products_get',
    )
    def get(self, request):
        # create new object
        products = Product.objects.all()

        # prepare response dto
        products_dto = [
            ProductRepresentation().get_dto(product) for product in products
        ]

        # validate response dto
        serializer = self.serializer_get_response(data=products_dto, many=True)
        if not serializer.is_valid():
            raise SerializationException(
                f'ProductDto[] serialization error: {serializer.errors}'
            )

        return Response(serializer.data)


class ProductGetUpdateDelete(APIView):
    serializer_patch_request = ProductUpdatePayloadSerializer
    serializer_patch_response = ProductDtoSerializer

    serializer_get_response = ProductDtoSerializer

    @extend_schema(
        responses={
            200: serializer_get_response(),
            400: ErrorResponseSerializer(),
            404: ErrorResponseSerializer(),
        },
        tags=['Products'],
        summary='Получить информацию о конкретном продукте',
        operation_id='product_get',
    )
    def get(self, request, id):
        # validate id
        if not is_valid_uuid(id):
            raise BadRequestException(f'{id} is not a valid UUID')

        # find existing object
        product = Product.objects.filter(id=id).first()

        if not product:
            raise ResourceNotFoundException(f'Product with id={id} not found')

        # prepare response dto
        product_dto = ProductRepresentation().get_dto(product)

        # validate response dto
        serializer = self.serializer_patch_response(data=product_dto)
        if not serializer.is_valid():
            raise SerializationException(
                f'ProductDto serialization error: {serializer.errors}'
            )

        return Response(serializer.data)

    @extend_schema(
        request=serializer_patch_request(),
        responses={
            200: serializer_patch_response(),
            400: ErrorResponseSerializer(),
            404: ErrorResponseSerializer(),
        },
        tags=['Products'],
        summary='Изменить существующий продукт',
        operation_id='product_patch',
    )
    def patch(self, request, id):
        # validate id
        if not is_valid_uuid(id):
            raise BadRequestException(f'{id} is not a valid UUID')

        # validate request data
        serializer = self.serializer_patch_request(data=request.data)

        if not serializer.is_valid():
            raise BadRequestException(str(serializer.errors))

        # find existing object
        product = Product.objects.filter(id=id).first()

        if not product:
            raise ResourceNotFoundException(f'Product with id={id} not found')

        # parse request data
        request_data = serializer.data

        is_active = request_data['is_active']

        # create new object
        product.is_active = is_active
        product.save()

        # prepare response dto
        product_dto = ProductRepresentation().get_dto(product)

        # validate response dto
        serializer = self.serializer_patch_response(data=product_dto)
        if not serializer.is_valid():
            raise SerializationException(
                f'ProductDto serialization error: {serializer.errors}'
            )

        return Response(serializer.data)

    @extend_schema(
        request=serializer_patch_request(),
        responses={
            204: None,
            400: ErrorResponseSerializer(),
            404: ErrorResponseSerializer(),
        },
        tags=['Products'],
        summary='Удалить существующий продукт',
        operation_id='product_delete',
    )
    def delete(self, request, id):
        # validate id
        if not is_valid_uuid(id):
            raise BadRequestException(f'{id} is not a valid UUID')

        # find existing object
        product = Product.objects.filter(id=id).first()

        if not product:
            raise ResourceNotFoundException(f'Product with id={id} not found')

        # delete existing object
        product.delete()

        return Response(status=204)
