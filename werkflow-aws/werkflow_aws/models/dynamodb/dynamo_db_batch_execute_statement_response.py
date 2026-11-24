from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_batch_statement_response import DynamoDBBatchStatementResponse
from .dynamo_db_consumed_capacity_model import DynamoDBConsumedCapacityModel


class DynamoDBBatchExecuteStatementResponse(BaseModel):
    Responses: list[DynamoDBBatchStatementResponse] | None = None
    ConsumedCapacity: list[DynamoDBConsumedCapacityModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
