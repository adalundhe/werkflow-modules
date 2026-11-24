from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionLabelAlias(BaseModel):
    Name: StrictStr | None = None
