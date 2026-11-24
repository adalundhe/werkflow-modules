from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value import DynamoDBAttributeValue


class DynamoDBItemResponse(BaseModel):
    Item: dict[StrictStr, DynamoDBAttributeValue] | None = None
