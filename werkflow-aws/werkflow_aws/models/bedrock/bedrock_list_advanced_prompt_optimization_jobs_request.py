from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListAdvancedPromptOptimizationJobsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: Literal['CreationTime'] | None = None
    sortOrder: Literal['Ascending', 'Descending'] | None = None
