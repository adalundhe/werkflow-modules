from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_bulk_operation_summary import DynamoDBBulkOperationSummary


class DynamoDBListBulkOperationsResponse(BaseModel):
    BulkOperationsSummaryList: list[DynamoDBBulkOperationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
