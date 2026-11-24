from __future__ import annotations
from pydantic import BaseModel
from .glue_code_gen_node_arg import GlueCodeGenNodeArg


class GlueLocation(BaseModel):
    Jdbc: list[GlueCodeGenNodeArg] | None = None
    S3: list[GlueCodeGenNodeArg] | None = None
    DynamoDB: list[GlueCodeGenNodeArg] | None = None
