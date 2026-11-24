from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSConnectionPoolConfigurationInfo(BaseModel):
    MaxConnectionsPercent: StrictInt | None = None
    MaxIdleConnectionsPercent: StrictInt | None = None
    ConnectionBorrowTimeout: StrictInt | None = None
    SessionPinningFilters: list[StrictStr] | None = None
    InitQuery: StrictStr | None = None
