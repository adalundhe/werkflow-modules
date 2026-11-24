from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_set_dimension import PinpointSetDimension


class PinpointSegmentDemographics(BaseModel):
    AppVersion: PinpointSetDimension | None = None
    Channel: PinpointSetDimension | None = None
    DeviceType: PinpointSetDimension | None = None
    Make: PinpointSetDimension | None = None
    Model: PinpointSetDimension | None = None
    Platform: PinpointSetDimension | None = None
