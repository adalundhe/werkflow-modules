from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_key_schema_element import DynamoDBKeySchemaElement
from .dynamo_db_projection import DynamoDBProjection


class DynamoDBLocalSecondaryIndexDescription(BaseModel):
    IndexName: StrictStr | None = None
    KeySchema: list[DynamoDBKeySchemaElement] | None = None
    Projection: DynamoDBProjection | None = None
    IndexSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    IndexArn: StrictStr | None = None
