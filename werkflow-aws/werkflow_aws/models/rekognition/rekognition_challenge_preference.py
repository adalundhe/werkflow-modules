from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .rekognition_versions import RekognitionVersions


class RekognitionChallengePreference(BaseModel):
    Type: Literal['FaceMovementAndLightChallenge', 'FaceMovementChallenge']
    Versions: RekognitionVersions | None = None
