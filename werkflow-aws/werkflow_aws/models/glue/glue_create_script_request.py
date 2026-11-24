from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .glue_code_gen_edge import GlueCodeGenEdge
from .glue_code_gen_node import GlueCodeGenNode


class GlueCreateScriptRequest(BaseModel):
    DagNodes: list[GlueCodeGenNode] | None = None
    DagEdges: list[GlueCodeGenEdge] | None = None
    Language: Literal['PYTHON', 'SCALA'] | None = None
