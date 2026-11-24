from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class GuardDutyCreateSampleFindingsResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
