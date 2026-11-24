from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_host import EC2Host


class EC2DescribeHostsResponse(BaseModel):
    Hosts: list[EC2Host] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
