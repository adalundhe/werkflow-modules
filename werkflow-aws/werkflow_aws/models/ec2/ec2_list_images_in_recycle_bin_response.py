from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_image_recycle_bin_info import EC2ImageRecycleBinInfo


class EC2ListImagesInRecycleBinResponse(BaseModel):
    Images: list[EC2ImageRecycleBinInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
