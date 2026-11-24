from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_known_gender import RekognitionKnownGender


class RekognitionGetCelebrityInfoResponse(BaseModel):
    Urls: list[StrictStr] | None = None
    Name: StrictStr | None = None
    KnownGender: RekognitionKnownGender | None = None
    ResponseMetadata: dict[str, Any] | None = None
