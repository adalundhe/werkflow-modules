from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateTerm(BaseModel):
    SourceText: StrictStr | None = None
    TargetText: StrictStr | None = None
