from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionFaceSearchSettings(BaseModel):
    CollectionId: StrictStr | None = None
    FaceMatchThreshold: StrictFloat | StrictInt | None = None
