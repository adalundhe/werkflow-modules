from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .detective_graph import DetectiveGraph


class DetectiveListGraphsResponse(BaseModel):
    GraphList: list[DetectiveGraph] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
