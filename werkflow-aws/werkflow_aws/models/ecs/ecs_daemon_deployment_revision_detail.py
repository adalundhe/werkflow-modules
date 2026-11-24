from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_daemon_deployment_capacity_provider import ECSDaemonDeploymentCapacityProvider


class ECSDaemonDeploymentRevisionDetail(BaseModel):
    arn: StrictStr | None = None
    capacityProviders: list[ECSDaemonDeploymentCapacityProvider] | None = None
    totalRunningInstanceCount: StrictInt | None = None
    totalWithoutDaemonInstanceCount: StrictInt | None = None
    totalDrainingInstanceCount: StrictInt | None = None
