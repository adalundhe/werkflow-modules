from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_byoasn import EC2Byoasn


class EC2DescribeIpamByoasnResponse(BaseModel):
    Byoasns: list[EC2Byoasn] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
