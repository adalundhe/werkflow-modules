from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_key_schema_element import DynamoDBKeySchemaElement
from .dynamo_db_projection import DynamoDBProjection


class DynamoDBLocalSecondaryIndex(BaseModel):
    IndexName: StrictStr
    KeySchema: list[DynamoDBKeySchemaElement]
    Projection: DynamoDBProjection
