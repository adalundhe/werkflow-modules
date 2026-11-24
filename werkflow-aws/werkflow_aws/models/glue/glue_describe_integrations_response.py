from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_integration import GlueIntegration


class GlueDescribeIntegrationsResponse(BaseModel):
    Integrations: list[GlueIntegration] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
