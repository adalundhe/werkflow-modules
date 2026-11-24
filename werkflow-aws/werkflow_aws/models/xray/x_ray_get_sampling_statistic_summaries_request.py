from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGetSamplingStatisticSummariesRequest(BaseModel):
    NextToken: StrictStr | None = None
