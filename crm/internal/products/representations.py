from crm.core.representations import Representation


class ProductRepresentation(Representation):
    def get_dto(self, model_instance):

        instance_dto = super(ProductRepresentation, self).get_dto(model_instance)

        # additional fields if needed
        pass

        return instance_dto
