from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeInboundIntegrationsRequest(BaseModel):
    IntegrationArn: StrictStr | None = None
    TargetArn: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
