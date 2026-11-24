from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeDBLogFilesRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    FilenameContains: StrictStr | None = None
    FileLastWritten: StrictInt | None = None
    FileSize: StrictInt | None = None
    Filters: list[RDSFilterModel] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
