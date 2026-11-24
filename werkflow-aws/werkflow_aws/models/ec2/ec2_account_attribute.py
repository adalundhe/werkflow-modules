from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_account_attribute_value import EC2AccountAttributeValue


class EC2AccountAttribute(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeValues: list[EC2AccountAttributeValue] | None = None
