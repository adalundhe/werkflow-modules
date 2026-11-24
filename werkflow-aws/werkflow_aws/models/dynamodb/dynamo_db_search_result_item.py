from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel


class DynamoDBSearchResultItem(BaseModel):
    Item: dict[StrictStr, DynamoDBAttributeValueModel] | None = None
    Score: StrictFloat | StrictInt | None = None
