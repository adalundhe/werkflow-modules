from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_conversion_task import EC2ConversionTask


class EC2ImportInstanceResponse(BaseModel):
    ConversionTask: EC2ConversionTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
