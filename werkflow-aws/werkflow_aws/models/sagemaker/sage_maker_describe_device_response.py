from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_edge_model import SageMakerEdgeModel


class SageMakerDescribeDeviceResponse(BaseModel):
    DeviceArn: StrictStr | None = None
    DeviceName: StrictStr | None = None
    Description: StrictStr | None = None
    DeviceFleetName: StrictStr | None = None
    IotThingName: StrictStr | None = None
    RegistrationTime: datetime.datetime | StrictStr | None = None
    LatestHeartbeat: datetime.datetime | StrictStr | None = None
    Models: list[SageMakerEdgeModel] | None = None
    MaxModels: StrictInt | None = None
    NextToken: StrictStr | None = None
    AgentVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
