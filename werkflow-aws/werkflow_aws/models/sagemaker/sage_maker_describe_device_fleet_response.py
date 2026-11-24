from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_edge_output_config import SageMakerEdgeOutputConfig


class SageMakerDescribeDeviceFleetResponse(BaseModel):
    DeviceFleetName: StrictStr | None = None
    DeviceFleetArn: StrictStr | None = None
    OutputConfig: SageMakerEdgeOutputConfig | None = None
    Description: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    RoleArn: StrictStr | None = None
    IotRoleAlias: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
