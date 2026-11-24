from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_deployment_stage import SageMakerDeploymentStage
from .sage_maker_edge_deployment_model_config import SageMakerEdgeDeploymentModelConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateEdgeDeploymentPlanRequest(BaseModel):
    EdgeDeploymentPlanName: StrictStr
    ModelConfigs: list[SageMakerEdgeDeploymentModelConfig]
    DeviceFleetName: StrictStr
    Stages: list[SageMakerDeploymentStage] | None = None
    Tags: list[SageMakerTagModel] | None = None
