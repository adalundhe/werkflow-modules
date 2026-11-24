from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_snapmirror_policy_filter import FSxSnapmirrorPolicyFilter


class FSxDescribeSnapmirrorPoliciesRequest(BaseModel):
    SnapmirrorPolicyIds: list[StrictStr] | None = None
    Filters: list[FSxSnapmirrorPolicyFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
