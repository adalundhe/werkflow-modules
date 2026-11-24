from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteTopicRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
