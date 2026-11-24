from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionParent(BaseModel):
    Name: StrictStr | None = None
