from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_statement import WAFv2Statement


class WAFv2AndStatement(BaseModel):
    Statements: list[WAFv2Statement] | None = None
