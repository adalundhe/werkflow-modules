from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_scheduling_policy_listing_detail import BatchSchedulingPolicyListingDetail


class BatchListSchedulingPoliciesResponse(BaseModel):
    schedulingPolicies: list[BatchSchedulingPolicyListingDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
