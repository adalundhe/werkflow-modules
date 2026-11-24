from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel


class DynamoDBBatchStatementRequest(BaseModel):
    Statement: StrictStr
    Parameters: list[DynamoDBAttributeValueModel] | None = None
    ConsistentRead: StrictBool | None = None
    ReturnValuesOnConditionCheckFailure: Literal['ALL_OLD', 'NONE'] | None = None
