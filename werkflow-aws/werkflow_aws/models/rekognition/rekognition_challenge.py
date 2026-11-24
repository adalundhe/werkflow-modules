from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionChallenge(BaseModel):
    Type: StrictStr | None = None
    Version: StrictStr | None = None
