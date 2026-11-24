from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionKnownGender(BaseModel):
    Type: StrictStr | None = None
