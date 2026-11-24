from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class IAMGetAccountSummaryResponse(BaseModel):
    SummaryMap: dict[StrictStr, StrictInt] | None = None
    ResponseMetadata: dict[str, Any] | None = None
