from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_human_loop_config import RekognitionHumanLoopConfig
from .rekognition_image import RekognitionImage


class RekognitionDetectModerationLabelsRequest(BaseModel):
    Image: RekognitionImage
    MinConfidence: StrictFloat | StrictInt | None = None
    HumanLoopConfig: RekognitionHumanLoopConfig | None = None
    ProjectVersion: StrictStr | None = None
