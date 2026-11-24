from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueDescribeInboundIntegrationsRequest(BaseModel):
    IntegrationArn: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    TargetArn: StrictStr | None = None
