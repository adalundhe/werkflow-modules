from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_ingress_vpc_configuration import AppRunnerIngressVpcConfiguration


class AppRunnerUpdateVpcIngressConnectionRequest(BaseModel):
    VpcIngressConnectionArn: StrictStr
    IngressVpcConfiguration: AppRunnerIngressVpcConfiguration
