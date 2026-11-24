from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AppFlowStartFlowResponse(BaseModel):
    flowArn: StrictStr | None = None
    flowStatus: StrictStr | None = None
    executionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
