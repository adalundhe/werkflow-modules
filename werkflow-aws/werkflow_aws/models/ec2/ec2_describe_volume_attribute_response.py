from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue
from .ec2_product_code import EC2ProductCode


class EC2DescribeVolumeAttributeResponse(BaseModel):
    AutoEnableIO: EC2AttributeBooleanValue | None = None
    ProductCodes: list[EC2ProductCode] | None = None
    VolumeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
