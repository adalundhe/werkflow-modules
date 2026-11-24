from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeQev2IdcApplicationsRequest(BaseModel):
    Qev2IdcApplicationArn: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
