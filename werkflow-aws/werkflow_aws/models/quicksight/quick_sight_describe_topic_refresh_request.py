from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeTopicRefreshRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    RefreshId: StrictStr
