from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerEdgeDeploymentPlanSummary(BaseModel):
    EdgeDeploymentPlanArn: StrictStr | None = None
    EdgeDeploymentPlanName: StrictStr | None = None
    DeviceFleetName: StrictStr | None = None
    EdgeDeploymentSuccess: StrictInt | None = None
    EdgeDeploymentPending: StrictInt | None = None
    EdgeDeploymentFailed: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
