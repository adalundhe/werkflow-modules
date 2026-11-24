from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_code_gen_edge import GlueCodeGenEdge
from .glue_code_gen_node import GlueCodeGenNode


class GlueGetDataflowGraphResponse(BaseModel):
    DagNodes: list[GlueCodeGenNode] | None = None
    DagEdges: list[GlueCodeGenEdge] | None = None
    ResponseMetadata: dict[str, Any] | None = None
