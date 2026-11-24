from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_service_link_virtual_interface import EC2ServiceLinkVirtualInterface


class EC2DescribeServiceLinkVirtualInterfacesResponse(BaseModel):
    ServiceLinkVirtualInterfaces: list[EC2ServiceLinkVirtualInterface] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
