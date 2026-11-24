from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2IpamPoolAllocation(BaseModel):
    Cidr: StrictStr | None = None
    IpamPoolAllocationId: StrictStr | None = None
    Description: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
