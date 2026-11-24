from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_runner_custom_domain import AppRunnerCustomDomain
from .app_runner_vpc_dns_target import AppRunnerVpcDNSTarget


class AppRunnerAssociateCustomDomainResponse(BaseModel):
    DNSTarget: StrictStr | None = None
    ServiceArn: StrictStr | None = None
    CustomDomain: AppRunnerCustomDomain | None = None
    VpcDNSTargets: list[AppRunnerVpcDNSTarget] | None = None
    ResponseMetadata: dict[str, Any] | None = None
