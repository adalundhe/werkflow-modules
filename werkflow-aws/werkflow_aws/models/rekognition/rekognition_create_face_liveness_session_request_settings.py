from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_challenge_preference import RekognitionChallengePreference
from .rekognition_liveness_output_config import RekognitionLivenessOutputConfig


class RekognitionCreateFaceLivenessSessionRequestSettings(BaseModel):
    OutputConfig: RekognitionLivenessOutputConfig | None = None
    AuditImagesLimit: StrictInt | None = None
    ChallengePreferences: list[RekognitionChallengePreference] | None = None
