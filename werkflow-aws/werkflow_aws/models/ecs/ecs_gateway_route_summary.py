from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSGatewayRouteSummary(BaseModel):
    gatewayRouteArn: StrictStr | None = None
    gatewayArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    serviceArn: StrictStr | None = None
    serviceContainerPortName: StrictStr | None = None
    status: StrictStr | None = None
