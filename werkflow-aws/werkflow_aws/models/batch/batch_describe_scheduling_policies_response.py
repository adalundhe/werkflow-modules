from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .batch_scheduling_policy_detail import BatchSchedulingPolicyDetail


class BatchDescribeSchedulingPoliciesResponse(BaseModel):
    schedulingPolicies: list[BatchSchedulingPolicyDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
