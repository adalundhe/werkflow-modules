from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeReservedNodeExchangeStatusRequest(BaseModel):
    ReservedNodeId: StrictStr | None = None
    ReservedNodeExchangeRequestId: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
