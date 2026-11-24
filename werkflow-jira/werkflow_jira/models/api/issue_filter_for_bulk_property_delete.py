from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class IssueFilterForBulkPropertyDelete(BaseModel):
    currentValue: Any = None
    entityIds: list[StrictInt] | None = None
