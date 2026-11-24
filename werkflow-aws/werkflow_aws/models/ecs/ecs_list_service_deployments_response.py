from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_service_deployment_brief import ECSServiceDeploymentBrief


class ECSListServiceDeploymentsResponse(BaseModel):
    serviceDeployments: list[ECSServiceDeploymentBrief] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
