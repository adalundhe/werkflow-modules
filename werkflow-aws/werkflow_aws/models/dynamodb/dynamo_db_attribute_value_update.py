from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_attribute_action import DynamoDBAttributeAction
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput


class DynamoDBAttributeValueUpdate(BaseModel):
    Value: DynamoDBAttributeValueInput | None = None
    Action: DynamoDBAttributeAction | None = None
