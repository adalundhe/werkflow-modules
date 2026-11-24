from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_batch_delete_knowledge_base_failure import QuickSightBatchDeleteKnowledgeBaseFailure
from .quick_sight_batch_delete_knowledge_base_success import QuickSightBatchDeleteKnowledgeBaseSuccess


class QuickSightBatchDeleteKnowledgeBaseResponse(BaseModel):
    Deleted: list[QuickSightBatchDeleteKnowledgeBaseSuccess] | None = None
    Errors: list[QuickSightBatchDeleteKnowledgeBaseFailure] | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
