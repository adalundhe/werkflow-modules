from __future__ import annotations
from pydantic import BaseModel
from .io_ts3_destination import IoTS3Destination


class IoTDestination(BaseModel):
    s3Destination: IoTS3Destination | None = None
