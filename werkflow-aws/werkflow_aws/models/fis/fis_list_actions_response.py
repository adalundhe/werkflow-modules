from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fis_action_summary import FISActionSummary


class FISListActionsResponse(BaseModel):
    actions: list[FISActionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
