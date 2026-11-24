from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_unsuccessful_face_deletion import RekognitionUnsuccessfulFaceDeletion


class RekognitionDeleteFacesResponse(BaseModel):
    DeletedFaces: list[StrictStr] | None = None
    UnsuccessfulFaceDeletions: list[RekognitionUnsuccessfulFaceDeletion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
