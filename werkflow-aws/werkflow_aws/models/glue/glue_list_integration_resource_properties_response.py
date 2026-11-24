from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_integration_resource_property import GlueIntegrationResourceProperty


class GlueListIntegrationResourcePropertiesResponse(BaseModel):
    IntegrationResourcePropertyList: list[GlueIntegrationResourceProperty] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
