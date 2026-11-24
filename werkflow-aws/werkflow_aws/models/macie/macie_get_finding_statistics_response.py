from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .macie_group_count import MacieGroupCount


class MacieGetFindingStatisticsResponse(BaseModel):
    countsByGroup: list[MacieGroupCount] | None = None
    ResponseMetadata: dict[str, Any] | None = None
