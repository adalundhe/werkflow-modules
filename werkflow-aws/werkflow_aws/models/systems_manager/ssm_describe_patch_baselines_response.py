from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_patch_baseline_identity import SSMPatchBaselineIdentity


class SSMDescribePatchBaselinesResponse(BaseModel):
    BaselineIdentities: list[SSMPatchBaselineIdentity] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
