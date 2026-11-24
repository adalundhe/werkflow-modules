from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_edge_model_summary import SageMakerEdgeModelSummary


class SageMakerDeviceSummary(BaseModel):
    DeviceName: StrictStr | None = None
    DeviceArn: StrictStr | None = None
    Description: StrictStr | None = None
    DeviceFleetName: StrictStr | None = None
    IotThingName: StrictStr | None = None
    RegistrationTime: datetime.datetime | StrictStr | None = None
    LatestHeartbeat: datetime.datetime | StrictStr | None = None
    Models: list[SageMakerEdgeModelSummary] | None = None
    AgentVersion: StrictStr | None = None
