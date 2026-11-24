from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayBatchGetTracesRequest(BaseModel):
    TraceIds: list[StrictStr]
    NextToken: StrictStr | None = None
