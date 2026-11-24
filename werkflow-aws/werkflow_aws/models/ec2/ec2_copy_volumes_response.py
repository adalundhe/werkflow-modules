from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_volume_model import EC2VolumeModel


class EC2CopyVolumesResponse(BaseModel):
    Volumes: list[EC2VolumeModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
