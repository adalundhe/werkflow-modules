from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeTopicV2Request(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
