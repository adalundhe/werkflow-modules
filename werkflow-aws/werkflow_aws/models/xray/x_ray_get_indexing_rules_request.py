from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGetIndexingRulesRequest(BaseModel):
    NextToken: StrictStr | None = None
