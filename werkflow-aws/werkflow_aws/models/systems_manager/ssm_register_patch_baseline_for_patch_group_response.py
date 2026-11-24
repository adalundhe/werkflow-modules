from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMRegisterPatchBaselineForPatchGroupResponse(BaseModel):
    BaselineId: StrictStr | None = None
    PatchGroup: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
