from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBPointInTimeRecoveryDescription(BaseModel):
    PointInTimeRecoveryStatus: StrictStr | None = None
    RecoveryPeriodInDays: StrictInt | None = None
    EarliestRestorableDateTime: datetime.datetime | StrictStr | None = None
    LatestRestorableDateTime: datetime.datetime | StrictStr | None = None
