REST_FRAMEWORK = {
    # 'EXCEPTION_HANDLER': 'crm.utils.errors.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'UNICODE_JSON': True,
    'DEFAULT_PERMISSION_CLASSES': [
        'crm.core.permissions.BasePermission',
    ],
    # Классы для изменения возвращаемых названий полей из snake_case в camelCase
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # Классы для изменения принимаемых названий полей из camelCase в snake_case
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'JSON_UNDERSCOREIZE': {
        # https://github.com/vbabiy/djangorestframework-camel-case#underscoreize-options
        'no_underscore_before_number': True,
    },
}
