from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_point_in_time_recovery_specification import DynamoDBPointInTimeRecoverySpecification


class DynamoDBUpdateContinuousBackupsRequest(BaseModel):
    TableName: StrictStr
    PointInTimeRecoverySpecification: DynamoDBPointInTimeRecoverySpecification
