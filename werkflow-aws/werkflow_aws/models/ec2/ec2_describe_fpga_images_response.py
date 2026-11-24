from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_fpga_image import EC2FpgaImage


class EC2DescribeFpgaImagesResponse(BaseModel):
    FpgaImages: list[EC2FpgaImage] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
