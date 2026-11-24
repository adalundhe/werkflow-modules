from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeTopicRefreshScheduleRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    DatasetId: StrictStr
