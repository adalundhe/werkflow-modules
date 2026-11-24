from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_consumed_capacity_model import DynamoDBConsumedCapacityModel
from .dynamo_db_item_response_model import DynamoDBItemResponseModel


class DynamoDBExecuteTransactionResponse(BaseModel):
    Responses: list[DynamoDBItemResponseModel] | None = None
    ConsumedCapacity: list[DynamoDBConsumedCapacityModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
