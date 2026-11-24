from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCodeGenEdge(BaseModel):
    Source: StrictStr | None = None
    Target: StrictStr | None = None
    TargetParameter: StrictStr | None = None
