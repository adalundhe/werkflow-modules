from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_create_face_liveness_session_request_settings import RekognitionCreateFaceLivenessSessionRequestSettings


class RekognitionCreateFaceLivenessSessionRequest(BaseModel):
    KmsKeyId: StrictStr | None = None
    Settings: RekognitionCreateFaceLivenessSessionRequestSettings | None = None
    ClientRequestToken: StrictStr | None = None
