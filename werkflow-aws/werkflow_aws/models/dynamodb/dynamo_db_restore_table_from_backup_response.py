from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_table_description_model import DynamoDBTableDescriptionModel


class DynamoDBRestoreTableFromBackupResponse(BaseModel):
    TableDescription: DynamoDBTableDescriptionModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
