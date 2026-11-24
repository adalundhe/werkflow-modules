from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_ingress_vpc_configuration import AppRunnerIngressVpcConfiguration
from .app_runner_tag import AppRunnerTag


class AppRunnerCreateVpcIngressConnectionRequest(BaseModel):
    ServiceArn: StrictStr
    VpcIngressConnectionName: StrictStr
    IngressVpcConfiguration: AppRunnerIngressVpcConfiguration
    Tags: list[AppRunnerTag] | None = None
