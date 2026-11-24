from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_routing_policy_registration import EC2IpamRoutingPolicyRegistration


class EC2GetIpamRoutingPolicyRegistrationsResponse(BaseModel):
    IpamRoutingPolicyRegistrations: list[EC2IpamRoutingPolicyRegistration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
