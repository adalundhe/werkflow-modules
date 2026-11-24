from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGetRetrievedTracesGraphRequest(BaseModel):
    RetrievalToken: StrictStr
    NextToken: StrictStr | None = None
