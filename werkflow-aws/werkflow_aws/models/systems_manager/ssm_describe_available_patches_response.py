from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_patch import SSMPatch


class SSMDescribeAvailablePatchesResponse(BaseModel):
    Patches: list[SSMPatch] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
