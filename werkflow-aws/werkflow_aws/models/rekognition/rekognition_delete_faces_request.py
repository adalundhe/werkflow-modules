from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDeleteFacesRequest(BaseModel):
    CollectionId: StrictStr
    FaceIds: list[StrictStr]
