from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_statement import GlueStatement


class GlueListStatementsResponse(BaseModel):
    Statements: list[GlueStatement] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
