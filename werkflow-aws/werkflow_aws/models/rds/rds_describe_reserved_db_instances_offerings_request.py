from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeReservedDBInstancesOfferingsRequest(BaseModel):
    ReservedDBInstancesOfferingId: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    Duration: StrictStr | None = None
    ProductDescription: StrictStr | None = None
    OfferingType: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    Filters: list[RDSFilterModel] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
