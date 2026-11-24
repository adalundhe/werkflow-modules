from __future__ import annotations
from pydantic import BaseModel
from .ec2_ipam_public_address_tag import EC2IpamPublicAddressTag


class EC2IpamPublicAddressTags(BaseModel):
    EipTags: list[EC2IpamPublicAddressTag] | None = None
