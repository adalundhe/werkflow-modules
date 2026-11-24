from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_nat_gateway_address import EC2NatGatewayAddress
from .ec2_nat_gateway_attached_appliance import EC2NatGatewayAttachedAppliance
from .ec2_provisioned_bandwidth import EC2ProvisionedBandwidth
from .ec2_tag_model import EC2TagModel


class EC2NatGateway(BaseModel):
    CreateTime: datetime.datetime | StrictStr | None = None
    DeleteTime: datetime.datetime | StrictStr | None = None
    FailureCode: StrictStr | None = None
    FailureMessage: StrictStr | None = None
    NatGatewayAddresses: list[EC2NatGatewayAddress] | None = None
    NatGatewayId: StrictStr | None = None
    ProvisionedBandwidth: EC2ProvisionedBandwidth | None = None
    State: StrictStr | None = None
    SubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ConnectivityType: StrictStr | None = None
    AvailabilityMode: StrictStr | None = None
    AutoScalingIps: StrictStr | None = None
    AutoProvisionZones: StrictStr | None = None
    AttachedAppliances: list[EC2NatGatewayAttachedAppliance] | None = None
    RouteTableId: StrictStr | None = None
