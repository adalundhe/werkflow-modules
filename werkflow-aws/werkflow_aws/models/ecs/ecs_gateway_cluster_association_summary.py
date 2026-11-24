from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSGatewayClusterAssociationSummary(BaseModel):
    gatewayArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    status: StrictStr | None = None
