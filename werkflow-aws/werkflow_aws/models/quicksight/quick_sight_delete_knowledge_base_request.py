from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteKnowledgeBaseRequest(BaseModel):
    AwsAccountId: StrictStr
    KnowledgeBaseId: StrictStr
