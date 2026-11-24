from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class CustomFieldValueUpdate(BaseModel):
    issueIds: list[StrictInt] | None = None
    value: Any = None
