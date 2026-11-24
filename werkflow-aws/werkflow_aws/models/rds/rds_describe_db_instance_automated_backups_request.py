from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeDBInstanceAutomatedBackupsRequest(BaseModel):
    DbiResourceId: StrictStr | None = None
    DBInstanceIdentifier: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    DBInstanceAutomatedBackupsArn: StrictStr | None = None
