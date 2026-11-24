from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_image import RekognitionImage


class RekognitionDetectCustomLabelsRequest(BaseModel):
    ProjectVersionArn: StrictStr
    Image: RekognitionImage
    MaxResults: StrictInt | None = None
    MinConfidence: StrictFloat | StrictInt | None = None
