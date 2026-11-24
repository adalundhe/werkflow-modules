from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_runner_ingress_vpc_configuration import AppRunnerIngressVpcConfiguration


class AppRunnerVpcIngressConnection(BaseModel):
    VpcIngressConnectionArn: StrictStr | None = None
    VpcIngressConnectionName: StrictStr | None = None
    ServiceArn: StrictStr | None = None
    Status: StrictStr | None = None
    AccountId: StrictStr | None = None
    DomainName: StrictStr | None = None
    IngressVpcConfiguration: AppRunnerIngressVpcConfiguration | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    DeletedAt: datetime.datetime | StrictStr | None = None
