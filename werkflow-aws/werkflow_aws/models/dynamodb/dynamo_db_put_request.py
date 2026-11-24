from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput


class DynamoDBPutRequest(BaseModel):
    Item: dict[StrictStr, DynamoDBAttributeValueInput]
