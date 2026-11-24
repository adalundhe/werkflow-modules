from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_integration import RedshiftIntegration


class RedshiftDescribeIntegrationsResponse(BaseModel):
    Marker: StrictStr | None = None
    Integrations: list[RedshiftIntegration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
