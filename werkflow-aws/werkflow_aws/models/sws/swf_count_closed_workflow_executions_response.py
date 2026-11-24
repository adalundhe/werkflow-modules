from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt


class SWFCountClosedWorkflowExecutionsResponse(BaseModel):
    count: StrictInt | None = None
    truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
