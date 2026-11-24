from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeKnowledgeBaseRequest(BaseModel):
    AwsAccountId: StrictStr
    KnowledgeBaseId: StrictStr
