from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_ipam_public_address_security_group import EC2IpamPublicAddressSecurityGroup
from .ec2_ipam_public_address_tags import EC2IpamPublicAddressTags


class EC2IpamDiscoveredPublicAddress(BaseModel):
    IpamResourceDiscoveryId: StrictStr | None = None
    AddressRegion: StrictStr | None = None
    Address: StrictStr | None = None
    AddressOwnerId: StrictStr | None = None
    AddressAllocationId: StrictStr | None = None
    AssociationStatus: StrictStr | None = None
    AddressType: StrictStr | None = None
    Service: StrictStr | None = None
    ServiceResource: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    PublicIpv4PoolId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    NetworkInterfaceDescription: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Tags: EC2IpamPublicAddressTags | None = None
    NetworkBorderGroup: StrictStr | None = None
    SecurityGroups: list[EC2IpamPublicAddressSecurityGroup] | None = None
    SampleTime: datetime.datetime | StrictStr | None = None
