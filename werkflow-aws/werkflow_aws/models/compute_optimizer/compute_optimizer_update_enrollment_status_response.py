from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ComputeOptimizerUpdateEnrollmentStatusResponse(BaseModel):
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
