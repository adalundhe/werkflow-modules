from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBatchDeleteKnowledgeBaseSuccess(BaseModel):
    KnowledgeBaseId: StrictStr | None = None
    KnowledgeBaseArn: StrictStr | None = None
