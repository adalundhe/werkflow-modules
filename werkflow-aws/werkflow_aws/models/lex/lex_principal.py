from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexPrincipal(BaseModel):
    service: StrictStr | None = None
    arn: StrictStr | None = None
