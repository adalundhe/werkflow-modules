from __future__ import annotations
from pydantic import BaseModel
from .glue_edge import GlueEdge
from .glue_node import GlueNode


class GlueWorkflowGraph(BaseModel):
    Nodes: list[GlueNode] | None = None
    Edges: list[GlueEdge] | None = None
