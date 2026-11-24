from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_time_to_live_status import DynamoDBTimeToLiveStatus


class DynamoDBTimeToLiveDescription(BaseModel):
    TimeToLiveStatus: DynamoDBTimeToLiveStatus | None = None
    AttributeName: StrictStr | None = None
