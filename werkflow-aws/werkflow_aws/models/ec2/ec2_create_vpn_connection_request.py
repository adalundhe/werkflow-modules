from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_vpn_connection_options_specification import EC2VpnConnectionOptionsSpecification


class EC2CreateVpnConnectionRequest(BaseModel):
    CustomerGatewayId: StrictStr
    Type: StrictStr
    VpnGatewayId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    VpnConcentratorId: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    PreSharedKeyStorage: StrictStr | None = None
    DryRun: StrictBool | None = None
    Options: EC2VpnConnectionOptionsSpecification | None = None
