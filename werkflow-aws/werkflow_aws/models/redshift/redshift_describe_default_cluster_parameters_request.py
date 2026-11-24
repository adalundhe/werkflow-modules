from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeDefaultClusterParametersRequest(BaseModel):
    ParameterGroupFamily: StrictStr
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
