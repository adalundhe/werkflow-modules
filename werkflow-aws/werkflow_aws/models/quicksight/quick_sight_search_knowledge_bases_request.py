from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_knowledge_base_search_filter import QuickSightKnowledgeBaseSearchFilter
from .quick_sight_knowledge_base_sort_by import QuickSightKnowledgeBaseSortBy


class QuickSightSearchKnowledgeBasesRequest(BaseModel):
    AwsAccountId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filters: list[QuickSightKnowledgeBaseSearchFilter] | None = None
    SortBy: QuickSightKnowledgeBaseSortBy | None = None
