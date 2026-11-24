from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel


class DynamoDBExecuteStatementRequest(BaseModel):
    Statement: StrictStr
    Parameters: list[DynamoDBAttributeValueModel] | None = None
    ConsistentRead: StrictBool | None = None
    NextToken: StrictStr | None = None
    ReturnConsumedCapacity: Literal['INDEXES', 'TOTAL', 'NONE'] | None = None
    Limit: StrictInt | None = None
    ReturnValuesOnConditionCheckFailure: Literal['ALL_OLD', 'NONE'] | None = None
