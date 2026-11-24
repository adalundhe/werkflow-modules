from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_secondary_interface import EC2SecondaryInterface


class EC2DescribeSecondaryInterfacesResponse(BaseModel):
    SecondaryInterfaces: list[EC2SecondaryInterface] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
