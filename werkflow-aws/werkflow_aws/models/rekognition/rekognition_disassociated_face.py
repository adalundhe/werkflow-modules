from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDisassociatedFace(BaseModel):
    FaceId: StrictStr | None = None
