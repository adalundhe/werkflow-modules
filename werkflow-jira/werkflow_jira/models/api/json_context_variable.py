from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class JsonContextVariable(BaseModel):
    type: StrictStr | None = None
    value: dict[StrictStr, Any] | None = None
