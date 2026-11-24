from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FSxDeleteSnapshotPolicyResponse(BaseModel):
    SnapshotPolicyId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
