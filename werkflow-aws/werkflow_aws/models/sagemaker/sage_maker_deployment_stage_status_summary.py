from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_device_selection_config import SageMakerDeviceSelectionConfig
from .sage_maker_edge_deployment_config import SageMakerEdgeDeploymentConfig
from .sage_maker_edge_deployment_status import SageMakerEdgeDeploymentStatus


class SageMakerDeploymentStageStatusSummary(BaseModel):
    StageName: StrictStr | None = None
    DeviceSelectionConfig: SageMakerDeviceSelectionConfig | None = None
    DeploymentConfig: SageMakerEdgeDeploymentConfig | None = None
    DeploymentStatus: SageMakerEdgeDeploymentStatus | None = None
