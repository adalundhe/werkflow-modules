from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightKnowledgeBaseSearchFilter(BaseModel):
    name: Literal['KNOWLEDGE_BASE_ID', 'KNOWLEDGE_BASE_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'KNOWLEDGE_BASE_SIZE_BYTES', 'PRIMARY_OWNER', 'DATASOURCE_ARN']
    operator: Literal['STRING_EQUALS', 'STRING_LIKE', 'GREATER_THAN_OR_EQUALS', 'LESS_THAN_OR_EQUALS']
    value: StrictStr
