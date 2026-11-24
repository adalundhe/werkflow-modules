from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_reserved_node import RedshiftReservedNode


class RedshiftAcceptReservedNodeExchangeResponse(BaseModel):
    ExchangedReservedNode: RedshiftReservedNode | None = None
    ResponseMetadata: dict[str, Any] | None = None
