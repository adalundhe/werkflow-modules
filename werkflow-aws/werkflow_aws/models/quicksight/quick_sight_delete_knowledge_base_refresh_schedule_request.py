from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteKnowledgeBaseRefreshScheduleRequest(BaseModel):
    AwsAccountId: StrictStr
    KnowledgeBaseId: StrictStr
    ScheduleId: StrictStr
