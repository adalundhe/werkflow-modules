from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_edge import SageMakerEdge
from .sage_maker_vertex import SageMakerVertex


class SageMakerQueryLineageResponse(BaseModel):
    Vertices: list[SageMakerVertex] | None = None
    Edges: list[SageMakerEdge] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
