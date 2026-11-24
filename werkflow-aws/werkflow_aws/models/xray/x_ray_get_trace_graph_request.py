from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGetTraceGraphRequest(BaseModel):
    TraceIds: list[StrictStr]
    NextToken: StrictStr | None = None
