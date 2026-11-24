from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMStartChangeRequestExecutionResponse(BaseModel):
    AutomationExecutionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
