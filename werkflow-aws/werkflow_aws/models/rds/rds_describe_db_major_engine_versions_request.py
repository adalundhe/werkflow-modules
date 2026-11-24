from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSDescribeDBMajorEngineVersionsRequest(BaseModel):
    Engine: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
