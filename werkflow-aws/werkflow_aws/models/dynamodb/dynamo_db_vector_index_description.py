from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_index_status import DynamoDBIndexStatus
from .dynamo_db_projection import DynamoDBProjection
from .dynamo_db_search_schema_element import DynamoDBSearchSchemaElement
from .dynamo_db_vector_attribute_definition import DynamoDBVectorAttributeDefinition
from .dynamo_db_vector_distance_function import DynamoDBVectorDistanceFunction


class DynamoDBVectorIndexDescription(BaseModel):
    IndexName: StrictStr | None = None
    SearchSchema: list[DynamoDBSearchSchemaElement] | None = None
    Projection: DynamoDBProjection | None = None
    VectorAttribute: DynamoDBVectorAttributeDefinition | None = None
    Dimensions: StrictInt | None = None
    DistanceFunction: DynamoDBVectorDistanceFunction | None = None
    IndexStatus: DynamoDBIndexStatus | None = None
    Backfilling: StrictBool | None = None
    IndexSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    IndexArn: StrictStr | None = None
