from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeExportTasksRequest(BaseModel):
    ExportTaskIdentifier: StrictStr | None = None
    SourceArn: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    SourceType: Literal['SNAPSHOT', 'CLUSTER'] | None = None
