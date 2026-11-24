from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_deployment_lifecycle_hook_timeout_configuration import ECSDeploymentLifecycleHookTimeoutConfiguration
from .ecs_hook_details import ECSHookDetails


class ECSDeploymentLifecycleHook(BaseModel):
    targetType: StrictStr | None = None
    hookTargetArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    lifecycleStages: list[StrictStr] | None = None
    hookDetails: ECSHookDetails | None = None
    timeoutConfiguration: ECSDeploymentLifecycleHookTimeoutConfiguration | None = None
