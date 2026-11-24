from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GuardDutyUpdateFilterResponse(BaseModel):
    Name: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
