from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .io_ts3_location import IoTS3Location


class IoTStreamFile(BaseModel):
    fileId: StrictInt | None = None
    s3Location: IoTS3Location | None = None
