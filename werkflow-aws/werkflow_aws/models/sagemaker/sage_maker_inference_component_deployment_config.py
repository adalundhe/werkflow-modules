from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_auto_rollback_config_model import SageMakerAutoRollbackConfigModel
from .sage_maker_inference_component_rolling_update_policy import SageMakerInferenceComponentRollingUpdatePolicy


class SageMakerInferenceComponentDeploymentConfig(BaseModel):
    RollingUpdatePolicy: SageMakerInferenceComponentRollingUpdatePolicy | None = None
    AutoRollbackConfiguration: SageMakerAutoRollbackConfigModel | None = None
