from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMGetPatchBaselineForPatchGroupResponse(BaseModel):
    BaselineId: StrictStr | None = None
    PatchGroup: StrictStr | None = None
    OperatingSystem: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
