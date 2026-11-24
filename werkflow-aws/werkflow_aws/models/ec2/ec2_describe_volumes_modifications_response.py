from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_volume_modification import EC2VolumeModification


class EC2DescribeVolumesModificationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    VolumesModifications: list[EC2VolumeModification] | None = None
    ResponseMetadata: dict[str, Any] | None = None
