from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class XRayListRetrievedTracesRequest(BaseModel):
    RetrievalToken: StrictStr
    TraceFormat: Literal['XRAY', 'OTEL'] | None = None
    NextToken: StrictStr | None = None
