from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerNetworkResourceUtilization(BaseModel):
    NetworkInBytesPerSecond: StrictStr | None = None
    NetworkOutBytesPerSecond: StrictStr | None = None
    NetworkPacketsInPerSecond: StrictStr | None = None
    NetworkPacketsOutPerSecond: StrictStr | None = None
