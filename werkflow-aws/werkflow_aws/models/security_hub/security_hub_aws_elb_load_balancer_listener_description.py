from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_elb_load_balancer_listener import SecurityHubAwsElbLoadBalancerListener


class SecurityHubAwsElbLoadBalancerListenerDescription(BaseModel):
    Listener: SecurityHubAwsElbLoadBalancerListener | None = None
    PolicyNames: list[StrictStr] | None = None
