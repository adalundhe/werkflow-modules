from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_global_table import DynamoDBGlobalTable


class DynamoDBListGlobalTablesResponse(BaseModel):
    GlobalTables: list[DynamoDBGlobalTable] | None = None
    LastEvaluatedGlobalTableName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
