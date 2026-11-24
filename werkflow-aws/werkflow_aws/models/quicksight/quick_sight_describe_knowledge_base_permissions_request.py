from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeKnowledgeBasePermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    KnowledgeBaseId: StrictStr
