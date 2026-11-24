from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_routing_policy_registration_delta import EC2IpamRoutingPolicyRegistrationDelta


class EC2GetIpamRoutingPolicyRegistrationDeltasResponse(BaseModel):
    IpamRoutingPolicyRegistrationDeltas: list[EC2IpamRoutingPolicyRegistrationDelta] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
