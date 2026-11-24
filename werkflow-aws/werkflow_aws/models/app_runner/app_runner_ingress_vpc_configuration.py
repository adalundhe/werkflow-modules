from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerIngressVpcConfiguration(BaseModel):
    VpcId: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
