from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_attribute_value import EC2AttributeValue


class EC2DhcpConfiguration(BaseModel):
    Key: StrictStr | None = None
    Values: list[EC2AttributeValue] | None = None
