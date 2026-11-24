from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerEdgeOverride(BaseModel):
    EdgeSets: list[list[StrictStr]] | None = None
    UseEdge: StrictStr | None = None
