from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_routing_policy_registration_delta import EC2IpamRoutingPolicyRegistrationDelta


class EC2BatchModifyIpamRoutingPolicyRegistrationsResponse(BaseModel):
    IpamRoutingPolicyRegistrationDelta: EC2IpamRoutingPolicyRegistrationDelta | None = None
    ResponseMetadata: dict[str, Any] | None = None
