from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_secondary_subnet import EC2SecondarySubnet


class EC2DeleteSecondarySubnetResponse(BaseModel):
    SecondarySubnet: EC2SecondarySubnet | None = None
    ClientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
