from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_secondary_interface_attachment import EC2SecondaryInterfaceAttachment
from .ec2_secondary_interface_ipv4_address import EC2SecondaryInterfaceIpv4Address
from .ec2_tag_model import EC2TagModel


class EC2SecondaryInterface(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Attachment: EC2SecondaryInterfaceAttachment | None = None
    MacAddress: StrictStr | None = None
    OwnerId: StrictStr | None = None
    PrivateIpv4Addresses: list[EC2SecondaryInterfaceIpv4Address] | None = None
    SecondaryInterfaceId: StrictStr | None = None
    SecondaryInterfaceArn: StrictStr | None = None
    SecondaryInterfaceType: StrictStr | None = None
    SecondarySubnetId: StrictStr | None = None
    SecondaryNetworkId: StrictStr | None = None
    SecondaryNetworkType: StrictStr | None = None
    SourceDestCheck: StrictBool | None = None
    Status: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
