from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_reserved_db_instance import RDSReservedDBInstance


class RDSPurchaseReservedDBInstancesOfferingResponse(BaseModel):
    ReservedDBInstance: RDSReservedDBInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
