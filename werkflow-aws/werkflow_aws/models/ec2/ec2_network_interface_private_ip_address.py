from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_network_interface_association import EC2NetworkInterfaceAssociation


class EC2NetworkInterfacePrivateIpAddress(BaseModel):
    Association: EC2NetworkInterfaceAssociation | None = None
    Primary: StrictBool | None = None
    PrivateDnsName: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
