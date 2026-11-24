from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_instance_patch_state import SSMInstancePatchState


class SSMDescribeInstancePatchStatesForPatchGroupResponse(BaseModel):
    InstancePatchStates: list[SSMInstancePatchState] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
