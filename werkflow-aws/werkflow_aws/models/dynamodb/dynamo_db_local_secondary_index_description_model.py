from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_key_schema_element_model import DynamoDBKeySchemaElementModel
from .dynamo_db_projection_model import DynamoDBProjectionModel


class DynamoDBLocalSecondaryIndexDescriptionModel(BaseModel):
    IndexName: StrictStr | None = None
    KeySchema: list[DynamoDBKeySchemaElementModel] | None = None
    Projection: DynamoDBProjectionModel | None = None
    IndexSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    IndexArn: StrictStr | None = None
