from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopEdgeDeploymentStageRequest(BaseModel):
    EdgeDeploymentPlanName: StrictStr
    StageName: StrictStr
