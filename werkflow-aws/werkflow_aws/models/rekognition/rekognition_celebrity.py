from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_compared_face import RekognitionComparedFace
from .rekognition_known_gender import RekognitionKnownGender


class RekognitionCelebrity(BaseModel):
    Urls: list[StrictStr] | None = None
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Face: RekognitionComparedFace | None = None
    MatchConfidence: StrictFloat | StrictInt | None = None
    KnownGender: RekognitionKnownGender | None = None
