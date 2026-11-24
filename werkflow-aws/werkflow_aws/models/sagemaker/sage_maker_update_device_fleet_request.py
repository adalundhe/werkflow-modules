from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_edge_output_config import SageMakerEdgeOutputConfig


class SageMakerUpdateDeviceFleetRequest(BaseModel):
    DeviceFleetName: StrictStr
    OutputConfig: SageMakerEdgeOutputConfig
    RoleArn: StrictStr | None = None
    Description: StrictStr | None = None
    EnableIotRoleAlias: StrictBool | None = None
