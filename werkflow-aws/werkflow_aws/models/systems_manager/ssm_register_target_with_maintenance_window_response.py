from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMRegisterTargetWithMaintenanceWindowResponse(BaseModel):
    WindowTargetId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
