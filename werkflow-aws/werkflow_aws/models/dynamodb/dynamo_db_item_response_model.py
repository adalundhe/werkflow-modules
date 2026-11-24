from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel


class DynamoDBItemResponseModel(BaseModel):
    Item: dict[StrictStr, DynamoDBAttributeValueModel] | None = None
