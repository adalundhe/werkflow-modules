from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_reserved_db_instance import RDSReservedDBInstance


class RDSDescribeReservedDBInstancesResponse(BaseModel):
    Marker: StrictStr | None = None
    ReservedDBInstances: list[RDSReservedDBInstance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
