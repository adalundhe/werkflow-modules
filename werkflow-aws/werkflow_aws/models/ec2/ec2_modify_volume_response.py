from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_volume_modification import EC2VolumeModification


class EC2ModifyVolumeResponse(BaseModel):
    VolumeModification: EC2VolumeModification | None = None
    ResponseMetadata: dict[str, Any] | None = None
