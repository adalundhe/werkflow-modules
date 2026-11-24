from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .dynamo_db_parameterized_statement import DynamoDBParameterizedStatement


class DynamoDBExecuteTransactionRequest(BaseModel):
    TransactStatements: list[DynamoDBParameterizedStatement]
    ClientRequestToken: StrictStr | None = None
    ReturnConsumedCapacity: Literal['INDEXES', 'TOTAL', 'NONE'] | None = None
