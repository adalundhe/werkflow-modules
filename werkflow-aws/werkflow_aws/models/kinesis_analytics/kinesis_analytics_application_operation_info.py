from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsApplicationOperationInfo(BaseModel):
    Operation: StrictStr | None = None
    OperationId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    OperationStatus: StrictStr | None = None
