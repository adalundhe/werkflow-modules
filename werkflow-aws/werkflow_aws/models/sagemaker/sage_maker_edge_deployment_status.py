from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerEdgeDeploymentStatus(BaseModel):
    StageStatus: StrictStr | None = None
    EdgeDeploymentSuccessInStage: StrictInt | None = None
    EdgeDeploymentPendingInStage: StrictInt | None = None
    EdgeDeploymentFailedInStage: StrictInt | None = None
    EdgeDeploymentStatusMessage: StrictStr | None = None
    EdgeDeploymentStageStartTime: datetime.datetime | StrictStr | None = None
