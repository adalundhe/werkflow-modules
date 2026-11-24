from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_associated_face import RekognitionAssociatedFace
from .rekognition_unsuccessful_face_association import RekognitionUnsuccessfulFaceAssociation


class RekognitionAssociateFacesResponse(BaseModel):
    AssociatedFaces: list[RekognitionAssociatedFace] | None = None
    UnsuccessfulFaceAssociations: list[RekognitionUnsuccessfulFaceAssociation] | None = None
    UserStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
