from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_mac_host import EC2MacHost


class EC2DescribeMacHostsResponse(BaseModel):
    MacHosts: list[EC2MacHost] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
