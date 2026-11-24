from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_content_type import RekognitionContentType
from .rekognition_human_loop_activation_output import RekognitionHumanLoopActivationOutput
from .rekognition_moderation_label import RekognitionModerationLabel


class RekognitionDetectModerationLabelsResponse(BaseModel):
    ModerationLabels: list[RekognitionModerationLabel] | None = None
    ModerationModelVersion: StrictStr | None = None
    HumanLoopActivationOutput: RekognitionHumanLoopActivationOutput | None = None
    ProjectVersion: StrictStr | None = None
    ContentTypes: list[RekognitionContentType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
