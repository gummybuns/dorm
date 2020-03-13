from .dynamo_search_interface import DynamoSearchInterface
from .search_attribute import DictAttribute
from ..dynamo_response import DynamoGetResponse


class DynamoGetInterface(DynamoSearchInterface):
    def execute(self):
        """TODO: need to validate all primary key / saerch keys are present"""
        response = self.client.get_item(**self.build())
        return DynamoGetResponse(response, self.reconstructor)

    def key(self, *expressions):
        for expression in expressions:
            key_dict = {}
            key_dict[expression.datatype.column_name] = expression.attribute_map()
            self.add_attribute(DictAttribute, 'Key', key_dict)
        return self