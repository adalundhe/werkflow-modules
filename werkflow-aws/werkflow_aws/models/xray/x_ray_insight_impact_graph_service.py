from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .x_ray_insight_impact_graph_edge import XRayInsightImpactGraphEdge


class XRayInsightImpactGraphService(BaseModel):
    ReferenceId: StrictInt | None = None
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    Names: list[StrictStr] | None = None
    AccountId: StrictStr | None = None
    Edges: list[XRayInsightImpactGraphEdge] | None = None
