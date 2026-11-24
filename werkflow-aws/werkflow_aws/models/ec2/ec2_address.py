from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2Address(BaseModel):
    AllocationId: StrictStr | None = None
    AssociationId: StrictStr | None = None
    Domain: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    NetworkInterfaceOwnerId: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    PublicIpv4Pool: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    CustomerOwnedIp: StrictStr | None = None
    CustomerOwnedIpv4Pool: StrictStr | None = None
    CarrierIp: StrictStr | None = None
    SubnetId: StrictStr | None = None
    ServiceManaged: StrictStr | None = None
    InstanceId: StrictStr | None = None
    PublicIp: StrictStr | None = None
