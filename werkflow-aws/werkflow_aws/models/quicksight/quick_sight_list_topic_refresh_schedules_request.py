from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightListTopicRefreshSchedulesRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
