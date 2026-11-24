from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_inbound_integration import GlueInboundIntegration


class GlueDescribeInboundIntegrationsResponse(BaseModel):
    InboundIntegrations: list[GlueInboundIntegration] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
