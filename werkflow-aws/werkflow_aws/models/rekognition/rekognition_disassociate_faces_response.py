from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_disassociated_face import RekognitionDisassociatedFace
from .rekognition_unsuccessful_face_disassociation import RekognitionUnsuccessfulFaceDisassociation


class RekognitionDisassociateFacesResponse(BaseModel):
    DisassociatedFaces: list[RekognitionDisassociatedFace] | None = None
    UnsuccessfulFaceDisassociations: list[RekognitionUnsuccessfulFaceDisassociation] | None = None
    UserStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
