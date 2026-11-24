from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftReservedNodeExchangeStatus(BaseModel):
    ReservedNodeExchangeRequestId: StrictStr | None = None
    Status: StrictStr | None = None
    RequestTime: datetime.datetime | StrictStr | None = None
    SourceReservedNodeId: StrictStr | None = None
    SourceReservedNodeType: StrictStr | None = None
    SourceReservedNodeCount: StrictInt | None = None
    TargetReservedNodeOfferingId: StrictStr | None = None
    TargetReservedNodeType: StrictStr | None = None
    TargetReservedNodeCount: StrictInt | None = None
