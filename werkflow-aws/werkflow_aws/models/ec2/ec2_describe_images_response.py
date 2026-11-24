from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_image import EC2Image


class EC2DescribeImagesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Images: list[EC2Image] | None = None
    ResponseMetadata: dict[str, Any] | None = None
