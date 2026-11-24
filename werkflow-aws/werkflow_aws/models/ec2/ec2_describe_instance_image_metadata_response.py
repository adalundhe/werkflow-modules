from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_image_metadata import EC2InstanceImageMetadata


class EC2DescribeInstanceImageMetadataResponse(BaseModel):
    InstanceImageMetadata: list[EC2InstanceImageMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
