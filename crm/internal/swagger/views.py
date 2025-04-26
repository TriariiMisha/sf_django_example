from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

schema_view_ws1 = SpectacularAPIView.as_view(
    api_version='ws1',
    urlconf='crm.urls',
    custom_settings={
        'TITLE': 'CRM API',
        'DESCRIPTION': 'API for CRM system',
        'SWAGGER_UI_DIST': 'SIDECAR',
        'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
        'VERSION': None,
        'CAMELIZE_NAMES': True,
        'POSTPROCESSING_HOOKS': [
            'drf_spectacular.hooks.postprocess_schema_enums',
            'drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields',
        ],
        'SCHEMA_PATH_PREFIX_TRIM': True,
        'SERVERS': [{'url': '/api/'}],
    },
    serve_public=True,
)

schema_view_ws1_swagger = SpectacularSwaggerView.as_view(
    url_name='schema',
)
