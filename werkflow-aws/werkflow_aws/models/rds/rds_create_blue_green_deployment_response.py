from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_blue_green_deployment import RDSBlueGreenDeployment


class RDSCreateBlueGreenDeploymentResponse(BaseModel):
    BlueGreenDeployment: RDSBlueGreenDeployment | None = None
    ResponseMetadata: dict[str, Any] | None = None
