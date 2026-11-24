from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsdb_instance import RDSDBInstance


class RDSDescribeDBInstancesResponse(BaseModel):
    Marker: StrictStr | None = None
    DBInstances: list[RDSDBInstance] | None = None
