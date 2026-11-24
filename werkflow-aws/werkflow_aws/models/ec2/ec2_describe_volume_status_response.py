from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_volume_status_item import EC2VolumeStatusItem


class EC2DescribeVolumeStatusResponse(BaseModel):
    NextToken: StrictStr | None = None
    VolumeStatuses: list[EC2VolumeStatusItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
