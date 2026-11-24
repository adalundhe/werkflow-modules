from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateVpcEndpointServiceConfigurationRequest(BaseModel):
    DryRun: StrictBool | None = None
    AcceptanceRequired: StrictBool | None = None
    PrivateDnsName: StrictStr | None = None
    NetworkLoadBalancerArns: list[StrictStr] | None = None
    GatewayLoadBalancerArns: list[StrictStr] | None = None
    SupportedIpAddressTypes: list[StrictStr] | None = None
    SupportedRegions: list[StrictStr] | None = None
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
