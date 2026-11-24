from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2LabelMatchStatement(BaseModel):
    Scope: StrictStr | None = None
    Key: StrictStr | None = None
