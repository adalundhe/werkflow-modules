from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_deployment_configuration import SageMakerDeploymentConfiguration


class SageMakerScheduledUpdateConfig(BaseModel):
    ScheduleExpression: StrictStr | None = None
    DeploymentConfig: SageMakerDeploymentConfiguration | None = None
