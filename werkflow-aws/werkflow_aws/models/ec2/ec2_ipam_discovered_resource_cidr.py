from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_ipam_resource_tag import EC2IpamResourceTag


class EC2IpamDiscoveredResourceCidr(BaseModel):
    IpamResourceDiscoveryId: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceOwnerId: StrictStr | None = None
    ResourceCidr: StrictStr | None = None
    IpSource: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceTags: list[EC2IpamResourceTag] | None = None
    IpUsage: StrictFloat | StrictInt | None = None
    VpcId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    NetworkInterfaceAttachmentStatus: StrictStr | None = None
    SampleTime: datetime.datetime | StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
