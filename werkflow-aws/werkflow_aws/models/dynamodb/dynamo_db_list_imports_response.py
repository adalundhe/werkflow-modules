from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_import_summary import DynamoDBImportSummary


class DynamoDBListImportsResponse(BaseModel):
    ImportSummaryList: list[DynamoDBImportSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
