from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_integration_filter import GlueIntegrationFilter


class GlueDescribeIntegrationsRequest(BaseModel):
    IntegrationIdentifier: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Filters: list[GlueIntegrationFilter] | None = None
