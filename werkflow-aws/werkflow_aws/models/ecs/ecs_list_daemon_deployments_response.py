from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_daemon_deployment_summary import ECSDaemonDeploymentSummary


class ECSListDaemonDeploymentsResponse(BaseModel):
    nextToken: StrictStr | None = None
    daemonDeployments: list[ECSDaemonDeploymentSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
