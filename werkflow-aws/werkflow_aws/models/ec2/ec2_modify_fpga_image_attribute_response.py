from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_fpga_image_attribute import EC2FpgaImageAttribute


class EC2ModifyFpgaImageAttributeResponse(BaseModel):
    FpgaImageAttribute: EC2FpgaImageAttribute | None = None
    ResponseMetadata: dict[str, Any] | None = None
