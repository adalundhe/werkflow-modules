from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DynamoDBArchivalSummary(BaseModel):
    ArchivalDateTime: datetime.datetime | None = None
    ArchivalReason: StrictStr | None = None
    ArchivalBackupArn: StrictStr | None = None
