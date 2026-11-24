from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel


class DynamoDBBatchStatementError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    Item: dict[StrictStr, DynamoDBAttributeValueModel] | None = None
