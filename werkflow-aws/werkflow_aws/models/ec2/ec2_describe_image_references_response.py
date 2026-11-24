from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_image_reference import EC2ImageReference


class EC2DescribeImageReferencesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ImageReferences: list[EC2ImageReference] | None = None
    ResponseMetadata: dict[str, Any] | None = None
