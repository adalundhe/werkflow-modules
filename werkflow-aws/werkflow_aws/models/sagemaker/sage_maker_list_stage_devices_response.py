from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_device_deployment_summary import SageMakerDeviceDeploymentSummary


class SageMakerListStageDevicesResponse(BaseModel):
    DeviceDeploymentSummaries: list[SageMakerDeviceDeploymentSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
