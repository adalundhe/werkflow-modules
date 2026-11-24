from __future__ import annotations
from pydantic import BaseModel
from .data_zone_s3_destination import DataZoneS3Destination


class DataZoneOutputLocation(BaseModel):
    s3: DataZoneS3Destination | None = None
