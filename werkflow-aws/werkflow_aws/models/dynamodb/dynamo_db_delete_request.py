from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput


class DynamoDBDeleteRequest(BaseModel):
    Key: dict[StrictStr, DynamoDBAttributeValueInput]
