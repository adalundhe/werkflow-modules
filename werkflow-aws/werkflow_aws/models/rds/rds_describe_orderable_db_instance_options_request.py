from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeOrderableDBInstanceOptionsRequest(BaseModel):
    Engine: StrictStr
    EngineVersion: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    AvailabilityZoneGroup: StrictStr | None = None
    Vpc: StrictBool | None = None
    Filters: list[RDSFilterModel] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
