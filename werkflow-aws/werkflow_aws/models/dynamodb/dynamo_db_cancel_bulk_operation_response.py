from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DynamoDBCancelBulkOperationResponse(BaseModel):
    BulkOperationArn: StrictStr | None = None
    BulkOperationStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
