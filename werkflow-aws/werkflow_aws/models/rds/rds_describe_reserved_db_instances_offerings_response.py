from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_reserved_db_instances_offering import RDSReservedDBInstancesOffering


class RDSDescribeReservedDBInstancesOfferingsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReservedDBInstancesOfferings: list[RDSReservedDBInstancesOffering] | None = None
    ResponseMetadata: dict[str, Any] | None = None
