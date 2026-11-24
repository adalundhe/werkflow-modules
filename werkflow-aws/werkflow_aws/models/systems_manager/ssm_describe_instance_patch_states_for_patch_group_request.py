from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_instance_patch_state_filter import SSMInstancePatchStateFilter


class SSMDescribeInstancePatchStatesForPatchGroupRequest(BaseModel):
    PatchGroup: StrictStr
    Filters: list[SSMInstancePatchStateFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
