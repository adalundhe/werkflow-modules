from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMGetDefaultPatchBaselineResponse(BaseModel):
    BaselineId: StrictStr | None = None
    OperatingSystem: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
