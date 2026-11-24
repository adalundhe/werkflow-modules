from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class GuardDutyUpdateIPSetResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
