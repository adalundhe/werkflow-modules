from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_daemon_deployment import ECSDaemonDeployment
from .ecs_failure import ECSFailure


class ECSDescribeDaemonDeploymentsResponse(BaseModel):
    failures: list[ECSFailure] | None = None
    daemonDeployments: list[ECSDaemonDeployment] | None = None
    ResponseMetadata: dict[str, Any] | None = None
