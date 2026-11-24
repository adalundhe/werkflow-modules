from __future__ import annotations
from pydantic import BaseModel
from .io_ts3_location import IoTS3Location


class IoTPackageVersionArtifact(BaseModel):
    s3Location: IoTS3Location | None = None
