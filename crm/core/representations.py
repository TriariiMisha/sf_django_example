from django.forms.models import model_to_dict

from crm.utils.converters import convert_ts_to_milliseconds


class Representation:
    def get_dto(self, model_instance):

        instance_dto = model_to_dict(model_instance)

        instance_dto['id'] = str(model_instance.id)
        instance_dto['created_at'] = convert_ts_to_milliseconds(
            model_instance.created_at
        )
        instance_dto['updated_at'] = convert_ts_to_milliseconds(
            model_instance.updated_at
        )

        return instance_dto
