from __future__ import annotations
from pydantic import BaseModel, StrictInt


class XRayInsightImpactGraphEdge(BaseModel):
    ReferenceId: StrictInt | None = None
