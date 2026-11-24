from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerVpcDNSTarget(BaseModel):
    VpcIngressConnectionArn: StrictStr | None = None
    VpcId: StrictStr | None = None
    DomainName: StrictStr | None = None
