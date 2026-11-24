from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionAssociatedFace(BaseModel):
    FaceId: StrictStr | None = None
