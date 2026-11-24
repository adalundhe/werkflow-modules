from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_canary_configuration import ECSCanaryConfiguration
from .ecs_deployment_alarms import ECSDeploymentAlarms
from .ecs_deployment_circuit_breaker import ECSDeploymentCircuitBreaker
from .ecs_deployment_early_success_criteria import ECSDeploymentEarlySuccessCriteria
from .ecs_deployment_lifecycle_hook import ECSDeploymentLifecycleHook
from .ecs_linear_configuration import ECSLinearConfiguration


class ECSDeploymentConfiguration(BaseModel):
    deploymentCircuitBreaker: ECSDeploymentCircuitBreaker | None = None
    maximumPercent: StrictInt | None = None
    minimumHealthyPercent: StrictInt | None = None
    alarms: ECSDeploymentAlarms | None = None
    strategy: StrictStr | None = None
    bakeTimeInMinutes: StrictInt | None = None
    lifecycleHooks: list[ECSDeploymentLifecycleHook] | None = None
    linearConfiguration: ECSLinearConfiguration | None = None
    canaryConfiguration: ECSCanaryConfiguration | None = None
    earlySuccessCriteria: ECSDeploymentEarlySuccessCriteria | None = None
