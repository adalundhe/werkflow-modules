from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel
from .dynamo_db_consumed_capacity_model import DynamoDBConsumedCapacityModel


class DynamoDBExecuteStatementResponse(BaseModel):
    Items: list[dict[StrictStr, DynamoDBAttributeValueModel]] | None = None
    NextToken: StrictStr | None = None
    ConsumedCapacity: DynamoDBConsumedCapacityModel | None = None
    LastEvaluatedKey: dict[StrictStr, DynamoDBAttributeValueModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
