from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_deployment_stage_status_summary import SageMakerDeploymentStageStatusSummary
from .sage_maker_edge_deployment_model_config import SageMakerEdgeDeploymentModelConfig


class SageMakerDescribeEdgeDeploymentPlanResponse(BaseModel):
    EdgeDeploymentPlanArn: StrictStr | None = None
    EdgeDeploymentPlanName: StrictStr | None = None
    ModelConfigs: list[SageMakerEdgeDeploymentModelConfig] | None = None
    DeviceFleetName: StrictStr | None = None
    EdgeDeploymentSuccess: StrictInt | None = None
    EdgeDeploymentPending: StrictInt | None = None
    EdgeDeploymentFailed: StrictInt | None = None
    Stages: list[SageMakerDeploymentStageStatusSummary] | None = None
    NextToken: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
