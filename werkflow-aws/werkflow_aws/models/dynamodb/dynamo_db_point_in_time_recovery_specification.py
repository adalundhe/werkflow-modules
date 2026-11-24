from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class DynamoDBPointInTimeRecoverySpecification(BaseModel):
    PointInTimeRecoveryEnabled: StrictBool
    RecoveryPeriodInDays: StrictInt | None = None
