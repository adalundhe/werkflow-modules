from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2RewriteConfig(BaseModel):
    Regex: StrictStr | None = None
    Replace: StrictStr | None = None
