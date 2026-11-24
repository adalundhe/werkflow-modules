from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_integration_table_properties_filter import GlueIntegrationTablePropertiesFilter


class GlueListIntegrationTablePropertiesRequest(BaseModel):
    Marker: StrictStr | None = None
    Filters: list[GlueIntegrationTablePropertiesFilter] | None = None
    MaxRecords: StrictInt | None = None
