from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerDeviceDeploymentSummary(BaseModel):
    EdgeDeploymentPlanArn: StrictStr | None = None
    EdgeDeploymentPlanName: StrictStr | None = None
    StageName: StrictStr | None = None
    DeployedStageName: StrictStr | None = None
    DeviceFleetName: StrictStr | None = None
    DeviceName: StrictStr | None = None
    DeviceArn: StrictStr | None = None
    DeviceDeploymentStatus: StrictStr | None = None
    DeviceDeploymentStatusMessage: StrictStr | None = None
    Description: StrictStr | None = None
    DeploymentStartTime: datetime.datetime | StrictStr | None = None
