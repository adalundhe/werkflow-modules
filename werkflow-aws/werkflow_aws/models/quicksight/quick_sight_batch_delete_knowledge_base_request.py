from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBatchDeleteKnowledgeBaseRequest(BaseModel):
    AwsAccountId: StrictStr
    KnowledgeBaseIds: list[StrictStr]
