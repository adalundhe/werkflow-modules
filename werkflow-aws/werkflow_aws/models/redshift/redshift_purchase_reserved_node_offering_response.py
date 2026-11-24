from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_reserved_node import RedshiftReservedNode


class RedshiftPurchaseReservedNodeOfferingResponse(BaseModel):
    ReservedNode: RedshiftReservedNode | None = None
    ResponseMetadata: dict[str, Any] | None = None
