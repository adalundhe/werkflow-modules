from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_device_fleet_summary import SageMakerDeviceFleetSummary


class SageMakerListDeviceFleetsResponse(BaseModel):
    DeviceFleetSummaries: list[SageMakerDeviceFleetSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
