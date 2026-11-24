from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerVpcIngressConnectionSummary(BaseModel):
    VpcIngressConnectionArn: StrictStr | None = None
    ServiceArn: StrictStr | None = None
