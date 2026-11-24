from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerListVpcIngressConnectionsFilter(BaseModel):
    ServiceArn: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
