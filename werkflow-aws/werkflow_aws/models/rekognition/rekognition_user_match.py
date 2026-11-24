from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_matched_user import RekognitionMatchedUser


class RekognitionUserMatch(BaseModel):
    Similarity: StrictFloat | StrictInt | None = None
    User: RekognitionMatchedUser | None = None
