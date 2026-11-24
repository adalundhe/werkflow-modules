from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecs_deployment_configuration import ECSDeploymentConfiguration
from .ecs_deployment_lifecycle_hook_detail import ECSDeploymentLifecycleHookDetail
from .ecs_rollback import ECSRollback
from .ecs_service_deployment_alarms import ECSServiceDeploymentAlarms
from .ecs_service_deployment_circuit_breaker import ECSServiceDeploymentCircuitBreaker
from .ecs_service_revision_summary import ECSServiceRevisionSummary


class ECSServiceDeployment(BaseModel):
    serviceDeploymentArn: StrictStr | None = None
    serviceArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    finishedAt: datetime.datetime | StrictStr | None = None
    stoppedAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    sourceServiceRevisions: list[ECSServiceRevisionSummary] | None = None
    targetServiceRevision: ECSServiceRevisionSummary | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    lifecycleStage: StrictStr | None = None
    lifecycleHookDetails: list[ECSDeploymentLifecycleHookDetail] | None = None
    deploymentConfiguration: ECSDeploymentConfiguration | None = None
    rollback: ECSRollback | None = None
    deploymentCircuitBreaker: ECSServiceDeploymentCircuitBreaker | None = None
    alarms: ECSServiceDeploymentAlarms | None = None
