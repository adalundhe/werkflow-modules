from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRecrawlPolicy(BaseModel):
    RecrawlBehavior: StrictStr | None = None
