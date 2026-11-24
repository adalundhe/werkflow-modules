from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ForgeAppPropertyResponse(BaseModel):
    key: StrictStr | None = None
    value: Any = None
