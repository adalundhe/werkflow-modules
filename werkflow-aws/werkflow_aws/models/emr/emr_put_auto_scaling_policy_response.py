from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_auto_scaling_policy_description import EMRAutoScalingPolicyDescription


class EMRPutAutoScalingPolicyResponse(BaseModel):
    ClusterId: StrictStr | None = None
    InstanceGroupId: StrictStr | None = None
    AutoScalingPolicy: EMRAutoScalingPolicyDescription | None = None
    ClusterArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
