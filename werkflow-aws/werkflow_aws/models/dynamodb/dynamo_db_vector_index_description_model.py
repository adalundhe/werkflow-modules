from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_projection_model import DynamoDBProjectionModel
from .dynamo_db_search_schema_element_model import DynamoDBSearchSchemaElementModel
from .dynamo_db_vector_attribute_definition_model import DynamoDBVectorAttributeDefinitionModel


class DynamoDBVectorIndexDescriptionModel(BaseModel):
    IndexName: StrictStr | None = None
    SearchSchema: list[DynamoDBSearchSchemaElementModel] | None = None
    Projection: DynamoDBProjectionModel | None = None
    VectorAttribute: DynamoDBVectorAttributeDefinitionModel | None = None
    Dimensions: StrictInt | None = None
    DistanceFunction: StrictStr | None = None
    IndexStatus: StrictStr | None = None
    Backfilling: StrictBool | None = None
    IndexSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    IndexArn: StrictStr | None = None
