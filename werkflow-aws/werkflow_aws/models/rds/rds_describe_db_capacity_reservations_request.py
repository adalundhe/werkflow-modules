from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeDBCapacityReservationsRequest(BaseModel):
    DBCapacityReservationIdentifier: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Filters: list[RDSFilterModel] | None = None
