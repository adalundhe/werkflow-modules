from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeTenantDatabasesRequest(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    TenantDBName: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
