from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecs_daemon_circuit_breaker import ECSDaemonCircuitBreaker
from .ecs_daemon_deployment_alarms import ECSDaemonDeploymentAlarms
from .ecs_daemon_deployment_configuration import ECSDaemonDeploymentConfiguration
from .ecs_daemon_deployment_revision_detail import ECSDaemonDeploymentRevisionDetail
from .ecs_daemon_rollback import ECSDaemonRollback


class ECSDaemonDeployment(BaseModel):
    daemonDeploymentArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    targetDaemonRevision: ECSDaemonDeploymentRevisionDetail | None = None
    sourceDaemonRevisions: list[ECSDaemonDeploymentRevisionDetail] | None = None
    circuitBreaker: ECSDaemonCircuitBreaker | None = None
    alarms: ECSDaemonDeploymentAlarms | None = None
    rollback: ECSDaemonRollback | None = None
    deploymentConfiguration: ECSDaemonDeploymentConfiguration | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    stoppedAt: datetime.datetime | StrictStr | None = None
    finishedAt: datetime.datetime | StrictStr | None = None
