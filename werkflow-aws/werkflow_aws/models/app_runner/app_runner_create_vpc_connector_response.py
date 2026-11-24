from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_runner_vpc_connector import AppRunnerVpcConnector


class AppRunnerCreateVpcConnectorResponse(BaseModel):
    VpcConnector: AppRunnerVpcConnector | None = None
    ResponseMetadata: dict[str, Any] | None = None
