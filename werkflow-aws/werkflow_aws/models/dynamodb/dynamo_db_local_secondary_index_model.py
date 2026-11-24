from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_key_schema_element_model import DynamoDBKeySchemaElementModel
from .dynamo_db_projection_model import DynamoDBProjectionModel


class DynamoDBLocalSecondaryIndexModel(BaseModel):
    IndexName: StrictStr
    KeySchema: list[DynamoDBKeySchemaElementModel]
    Projection: DynamoDBProjectionModel
