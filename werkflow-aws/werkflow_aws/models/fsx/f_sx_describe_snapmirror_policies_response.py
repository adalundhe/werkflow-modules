from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_snapmirror_policy import FSxSnapmirrorPolicy


class FSxDescribeSnapmirrorPoliciesResponse(BaseModel):
    SnapmirrorPolicies: list[FSxSnapmirrorPolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
