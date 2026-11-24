from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_runner_vpc_ingress_connection import AppRunnerVpcIngressConnection


class AppRunnerCreateVpcIngressConnectionResponse(BaseModel):
    VpcIngressConnection: AppRunnerVpcIngressConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
