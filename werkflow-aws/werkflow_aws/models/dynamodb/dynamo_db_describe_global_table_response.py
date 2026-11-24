from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_global_table_description import DynamoDBGlobalTableDescription


class DynamoDBDescribeGlobalTableResponse(BaseModel):
    GlobalTableDescription: DynamoDBGlobalTableDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
