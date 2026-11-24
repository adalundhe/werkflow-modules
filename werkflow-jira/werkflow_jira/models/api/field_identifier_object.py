from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FieldIdentifierObject(BaseModel):
    identifier: dict[StrictStr, Any] | None = None
    type: StrictStr | None = None
