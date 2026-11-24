from __future__ import annotations
from pydantic import BaseModel
from .io_ts3_location import IoTS3Location
from .io_t_stream import IoTStream


class IoTFileLocation(BaseModel):
    stream: IoTStream | None = None
    s3Location: IoTS3Location | None = None
