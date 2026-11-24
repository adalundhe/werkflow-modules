from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_auto_rollback_config import SageMakerAutoRollbackConfig
from .sage_maker_blue_green_update_policy import SageMakerBlueGreenUpdatePolicy
from .sage_maker_rolling_update_policy import SageMakerRollingUpdatePolicy


class SageMakerDeploymentConfig(BaseModel):
    BlueGreenUpdatePolicy: SageMakerBlueGreenUpdatePolicy | None = None
    RollingUpdatePolicy: SageMakerRollingUpdatePolicy | None = None
    AutoRollbackConfiguration: SageMakerAutoRollbackConfig | None = None
