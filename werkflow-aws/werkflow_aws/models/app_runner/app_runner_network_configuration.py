from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_egress_configuration import AppRunnerEgressConfiguration
from .app_runner_ingress_configuration import AppRunnerIngressConfiguration


class AppRunnerNetworkConfiguration(BaseModel):
    EgressConfiguration: AppRunnerEgressConfiguration | None = None
    IngressConfiguration: AppRunnerIngressConfiguration | None = None
    IpAddressType: StrictStr | None = None
