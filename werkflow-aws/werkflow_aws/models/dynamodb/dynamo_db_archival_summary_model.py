from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DynamoDBArchivalSummaryModel(BaseModel):
    ArchivalDateTime: datetime.datetime | StrictStr | None = None
    ArchivalReason: StrictStr | None = None
    ArchivalBackupArn: StrictStr | None = None
