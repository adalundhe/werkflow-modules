from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_inbound_integration import RedshiftInboundIntegration


class RedshiftDescribeInboundIntegrationsResponse(BaseModel):
    Marker: StrictStr | None = None
    InboundIntegrations: list[RedshiftInboundIntegration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
