from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BatchCreateComputeEnvironmentResponse(BaseModel):
    computeEnvironmentName: StrictStr | None = None
    computeEnvironmentArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
