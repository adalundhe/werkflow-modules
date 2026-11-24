from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteEdgeDeploymentPlanRequest(BaseModel):
    EdgeDeploymentPlanName: StrictStr
