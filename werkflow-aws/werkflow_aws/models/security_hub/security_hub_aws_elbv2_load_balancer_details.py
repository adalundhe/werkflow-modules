from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_availability_zone import SecurityHubAvailabilityZone
from .security_hub_aws_elbv2_load_balancer_attribute import SecurityHubAwsElbv2LoadBalancerAttribute
from .security_hub_load_balancer_state import SecurityHubLoadBalancerState


class SecurityHubAwsElbv2LoadBalancerDetails(BaseModel):
    AvailabilityZones: list[SecurityHubAvailabilityZone] | None = None
    CanonicalHostedZoneId: StrictStr | None = None
    CreatedTime: StrictStr | None = None
    DNSName: StrictStr | None = None
    IpAddressType: StrictStr | None = None
    Scheme: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    State: SecurityHubLoadBalancerState | None = None
    Type: StrictStr | None = None
    VpcId: StrictStr | None = None
    LoadBalancerAttributes: list[SecurityHubAwsElbv2LoadBalancerAttribute] | None = None
