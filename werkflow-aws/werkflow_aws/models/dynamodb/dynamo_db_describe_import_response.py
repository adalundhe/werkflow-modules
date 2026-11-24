from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_import_table_description import DynamoDBImportTableDescription


class DynamoDBDescribeImportResponse(BaseModel):
    ImportTableDescription: DynamoDBImportTableDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
