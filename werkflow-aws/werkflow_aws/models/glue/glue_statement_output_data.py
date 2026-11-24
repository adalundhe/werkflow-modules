from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStatementOutputData(BaseModel):
    TextPlain: StrictStr | None = None
