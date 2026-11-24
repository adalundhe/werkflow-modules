from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_failure import ECSFailure
from .ecs_service_deployment import ECSServiceDeployment


class ECSDescribeServiceDeploymentsResponse(BaseModel):
    serviceDeployments: list[ECSServiceDeployment] | None = None
    failures: list[ECSFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
