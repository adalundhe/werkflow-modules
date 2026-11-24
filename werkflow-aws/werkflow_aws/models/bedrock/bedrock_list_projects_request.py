from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListProjectsRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    statusFilter: Literal['active', 'archived'] | None = None
