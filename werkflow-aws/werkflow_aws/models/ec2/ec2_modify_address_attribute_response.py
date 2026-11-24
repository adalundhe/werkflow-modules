from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_address_attribute import EC2AddressAttribute


class EC2ModifyAddressAttributeResponse(BaseModel):
    Address: EC2AddressAttribute | None = None
    ResponseMetadata: dict[str, Any] | None = None
