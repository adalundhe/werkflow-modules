from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueForgeObjectField(BaseModel):
    contextId: StrictStr | None = None
    object: dict[StrictStr, Any] | None = None
    type: StrictStr | None = None
