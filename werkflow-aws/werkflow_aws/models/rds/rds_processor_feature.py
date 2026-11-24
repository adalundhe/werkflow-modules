from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSProcessorFeature(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
