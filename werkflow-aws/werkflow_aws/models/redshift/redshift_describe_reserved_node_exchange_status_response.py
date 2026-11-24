from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_reserved_node_exchange_status import RedshiftReservedNodeExchangeStatus


class RedshiftDescribeReservedNodeExchangeStatusResponse(BaseModel):
    ReservedNodeExchangeStatusDetails: list[RedshiftReservedNodeExchangeStatus] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
