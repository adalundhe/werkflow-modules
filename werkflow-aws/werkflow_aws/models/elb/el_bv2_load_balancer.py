from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .el_bv2_availability_zone import ELBv2AvailabilityZone
from .el_bv2_ipam_pools import ELBv2IpamPools
from .el_bv2_load_balancer_state import ELBv2LoadBalancerState


class ELBv2LoadBalancer(BaseModel):
    LoadBalancerArn: StrictStr | None = None
    DNSName: StrictStr | None = None
    CanonicalHostedZoneId: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LoadBalancerName: StrictStr | None = None
    Scheme: StrictStr | None = None
    VpcId: StrictStr | None = None
    State: ELBv2LoadBalancerState | None = None
    Type: StrictStr | None = None
    AvailabilityZones: list[ELBv2AvailabilityZone] | None = None
    SecurityGroups: list[StrictStr] | None = None
    IpAddressType: StrictStr | None = None
    CustomerOwnedIpv4Pool: StrictStr | None = None
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: StrictStr | None = None
    EnablePrefixForIpv6SourceNat: StrictStr | None = None
    IpamPools: ELBv2IpamPools | None = None
