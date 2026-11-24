from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_describe_fast_launch_images_success_item import EC2DescribeFastLaunchImagesSuccessItem


class EC2DescribeFastLaunchImagesResponse(BaseModel):
    FastLaunchImages: list[EC2DescribeFastLaunchImagesSuccessItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
