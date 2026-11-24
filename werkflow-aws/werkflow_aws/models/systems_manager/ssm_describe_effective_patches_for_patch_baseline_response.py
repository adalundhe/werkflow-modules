from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_effective_patch import SSMEffectivePatch


class SSMDescribeEffectivePatchesForPatchBaselineResponse(BaseModel):
    EffectivePatches: list[SSMEffectivePatch] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
