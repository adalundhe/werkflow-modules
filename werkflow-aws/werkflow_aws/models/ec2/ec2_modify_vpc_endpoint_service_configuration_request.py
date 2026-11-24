from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpcEndpointServiceConfigurationRequest(BaseModel):
    ServiceId: StrictStr
    DryRun: StrictBool | None = None
    PrivateDnsName: StrictStr | None = None
    RemovePrivateDnsName: StrictBool | None = None
    AcceptanceRequired: StrictBool | None = None
    AddNetworkLoadBalancerArns: list[StrictStr] | None = None
    RemoveNetworkLoadBalancerArns: list[StrictStr] | None = None
    AddGatewayLoadBalancerArns: list[StrictStr] | None = None
    RemoveGatewayLoadBalancerArns: list[StrictStr] | None = None
    AddSupportedIpAddressTypes: list[StrictStr] | None = None
    RemoveSupportedIpAddressTypes: list[StrictStr] | None = None
    AddSupportedRegions: list[StrictStr] | None = None
    RemoveSupportedRegions: list[StrictStr] | None = None
