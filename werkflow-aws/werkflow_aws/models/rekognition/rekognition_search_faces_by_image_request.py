from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_image import RekognitionImage


class RekognitionSearchFacesByImageRequest(BaseModel):
    CollectionId: StrictStr
    Image: RekognitionImage
    MaxFaces: StrictInt | None = None
    FaceMatchThreshold: StrictFloat | StrictInt | None = None
    QualityFilter: Literal['NONE', 'AUTO', 'LOW', 'MEDIUM', 'HIGH'] | None = None
