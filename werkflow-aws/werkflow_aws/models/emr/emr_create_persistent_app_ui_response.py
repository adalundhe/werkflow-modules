from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EMRCreatePersistentAppUIResponse(BaseModel):
    PersistentAppUIId: StrictStr | None = None
    RuntimeRoleEnabledCluster: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
