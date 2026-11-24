from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGetSamplingRulesRequest(BaseModel):
    NextToken: StrictStr | None = None
