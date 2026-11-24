from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_export_description import DynamoDBExportDescription


class DynamoDBDescribeExportResponse(BaseModel):
    ExportDescription: DynamoDBExportDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
