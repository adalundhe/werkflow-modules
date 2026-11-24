from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DynamoDBBulkOperationSummary(BaseModel):
    BulkOperationArn: StrictStr | None = None
    BulkOperationStatus: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
