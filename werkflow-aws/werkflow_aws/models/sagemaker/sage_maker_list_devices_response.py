from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_device_summary import SageMakerDeviceSummary


class SageMakerListDevicesResponse(BaseModel):
    DeviceSummaries: list[SageMakerDeviceSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
