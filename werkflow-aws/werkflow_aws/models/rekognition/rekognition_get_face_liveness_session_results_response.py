from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_audit_image import RekognitionAuditImage
from .rekognition_challenge import RekognitionChallenge
from .rekognition_feedback_item import RekognitionFeedbackItem
from .rekognition_session_metadata import RekognitionSessionMetadata


class RekognitionGetFaceLivenessSessionResultsResponse(BaseModel):
    SessionId: StrictStr | None = None
    Status: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    ReferenceImage: RekognitionAuditImage | None = None
    AuditImages: list[RekognitionAuditImage] | None = None
    Challenge: RekognitionChallenge | None = None
    Feedback: list[RekognitionFeedbackItem] | None = None
    Metadata: RekognitionSessionMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
