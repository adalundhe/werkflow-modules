from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_statement import GlueStatement


class GlueGetStatementResponse(BaseModel):
    Statement: GlueStatement | None = None
    ResponseMetadata: dict[str, Any] | None = None
