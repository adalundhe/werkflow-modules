from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_integration import RDSIntegration


class RDSDescribeIntegrationsResponse(BaseModel):
    Marker: StrictStr | None = None
    Integrations: list[RDSIntegration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
