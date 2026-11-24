from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_deployment_stage import SageMakerDeploymentStage


class SageMakerCreateEdgeDeploymentStageRequest(BaseModel):
    EdgeDeploymentPlanName: StrictStr
    Stages: list[SageMakerDeploymentStage]
