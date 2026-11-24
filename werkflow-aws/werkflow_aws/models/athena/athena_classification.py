from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaClassification(BaseModel):
    Name: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
