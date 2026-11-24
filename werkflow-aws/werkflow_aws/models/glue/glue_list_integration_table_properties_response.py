from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_integration_table_properties import GlueIntegrationTableProperties


class GlueListIntegrationTablePropertiesResponse(BaseModel):
    IntegrationTablePropertiesList: list[GlueIntegrationTableProperties] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
