from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeTopicRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
