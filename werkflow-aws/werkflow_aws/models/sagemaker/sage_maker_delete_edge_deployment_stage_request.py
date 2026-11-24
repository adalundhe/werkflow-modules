from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteEdgeDeploymentStageRequest(BaseModel):
    EdgeDeploymentPlanName: StrictStr
    StageName: StrictStr
