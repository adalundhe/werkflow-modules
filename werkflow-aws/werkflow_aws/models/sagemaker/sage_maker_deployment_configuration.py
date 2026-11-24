from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_alarm_details import SageMakerAlarmDetails
from .sage_maker_rolling_deployment_policy import SageMakerRollingDeploymentPolicy


class SageMakerDeploymentConfiguration(BaseModel):
    RollingUpdatePolicy: SageMakerRollingDeploymentPolicy | None = None
    WaitIntervalInSeconds: StrictInt | None = None
    AutoRollbackConfiguration: list[SageMakerAlarmDetails] | None = None
