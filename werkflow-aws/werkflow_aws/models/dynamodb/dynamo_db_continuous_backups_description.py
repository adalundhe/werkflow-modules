from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_point_in_time_recovery_description import DynamoDBPointInTimeRecoveryDescription


class DynamoDBContinuousBackupsDescription(BaseModel):
    ContinuousBackupsStatus: StrictStr | None = None
    PointInTimeRecoveryDescription: DynamoDBPointInTimeRecoveryDescription | None = None
