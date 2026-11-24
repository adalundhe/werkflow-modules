from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_integration_resource_property_filter import GlueIntegrationResourcePropertyFilter


class GlueListIntegrationResourcePropertiesRequest(BaseModel):
    Marker: StrictStr | None = None
    Filters: list[GlueIntegrationResourcePropertyFilter] | None = None
    MaxRecords: StrictInt | None = None
