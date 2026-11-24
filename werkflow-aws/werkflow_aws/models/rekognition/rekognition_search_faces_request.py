from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionSearchFacesRequest(BaseModel):
    CollectionId: StrictStr
    FaceId: StrictStr
    MaxFaces: StrictInt | None = None
    FaceMatchThreshold: StrictFloat | StrictInt | None = None
