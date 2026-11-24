from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_device_selection_config import SageMakerDeviceSelectionConfig
from .sage_maker_edge_deployment_config import SageMakerEdgeDeploymentConfig


class SageMakerDeploymentStage(BaseModel):
    StageName: StrictStr
    DeviceSelectionConfig: SageMakerDeviceSelectionConfig
    DeploymentConfig: SageMakerEdgeDeploymentConfig | None = None
