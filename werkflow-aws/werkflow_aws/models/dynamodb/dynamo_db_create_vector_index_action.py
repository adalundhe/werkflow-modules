from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_projection import DynamoDBProjection
from .dynamo_db_search_schema_element import DynamoDBSearchSchemaElement
from .dynamo_db_vector_attribute_definition import DynamoDBVectorAttributeDefinition
from .dynamo_db_vector_distance_function import DynamoDBVectorDistanceFunction


class DynamoDBCreateVectorIndexAction(BaseModel):
    IndexName: StrictStr
    VectorAttribute: DynamoDBVectorAttributeDefinition
    Projection: DynamoDBProjection
    Dimensions: StrictInt
    DistanceFunction: DynamoDBVectorDistanceFunction
    SearchSchema: list[DynamoDBSearchSchemaElement] | None = None
