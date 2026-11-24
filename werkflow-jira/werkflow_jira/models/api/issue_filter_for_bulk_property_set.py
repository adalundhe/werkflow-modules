from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt


class IssueFilterForBulkPropertySet(BaseModel):
    currentValue: Any = None
    entityIds: list[StrictInt] | None = None
    hasProperty: StrictBool | None = None
