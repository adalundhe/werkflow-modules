from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGraphLink(BaseModel):
    ReferenceType: StrictStr | None = None
    SourceTraceId: StrictStr | None = None
    DestinationTraceIds: list[StrictStr] | None = None
