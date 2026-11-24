from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStartEdgeDeploymentStageRequest(BaseModel):
    EdgeDeploymentPlanName: StrictStr
    StageName: StrictStr
