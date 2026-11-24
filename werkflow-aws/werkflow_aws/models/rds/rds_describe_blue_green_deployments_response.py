from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_blue_green_deployment import RDSBlueGreenDeployment


class RDSDescribeBlueGreenDeploymentsResponse(BaseModel):
    BlueGreenDeployments: list[RDSBlueGreenDeployment] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
