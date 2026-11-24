from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionSearchedFace(BaseModel):
    FaceId: StrictStr | None = None
