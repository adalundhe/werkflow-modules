from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_patch_group_patch_baseline_mapping import SSMPatchGroupPatchBaselineMapping


class SSMDescribePatchGroupsResponse(BaseModel):
    Mappings: list[SSMPatchGroupPatchBaselineMapping] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
