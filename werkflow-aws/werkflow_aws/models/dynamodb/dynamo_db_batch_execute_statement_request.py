from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .dynamo_db_batch_statement_request import DynamoDBBatchStatementRequest


class DynamoDBBatchExecuteStatementRequest(BaseModel):
    Statements: list[DynamoDBBatchStatementRequest]
    ReturnConsumedCapacity: Literal['INDEXES', 'TOTAL', 'NONE'] | None = None
