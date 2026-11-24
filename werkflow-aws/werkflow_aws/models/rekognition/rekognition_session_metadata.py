from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionSessionMetadata(BaseModel):
    SDKType: StrictStr | None = None
