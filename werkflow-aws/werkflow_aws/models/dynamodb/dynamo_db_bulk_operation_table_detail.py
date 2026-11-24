from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBBulkOperationTableDetail(BaseModel):
    TableName: StrictStr | None = None
    TableId: StrictStr | None = None
