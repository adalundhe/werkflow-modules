from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTopicReference(BaseModel):
    TopicPlaceholder: StrictStr
    TopicArn: StrictStr
