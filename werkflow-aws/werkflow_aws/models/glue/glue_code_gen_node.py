from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_code_gen_node_arg import GlueCodeGenNodeArg


class GlueCodeGenNode(BaseModel):
    Id: StrictStr | None = None
    NodeType: StrictStr | None = None
    Args: list[GlueCodeGenNodeArg] | None = None
    LineNumber: StrictInt | None = None
