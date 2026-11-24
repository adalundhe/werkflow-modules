from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMGetCalendarStateResponse(BaseModel):
    State: StrictStr | None = None
    AtTime: StrictStr | None = None
    NextTransitionTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
