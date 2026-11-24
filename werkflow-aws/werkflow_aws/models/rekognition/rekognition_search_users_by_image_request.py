from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_image import RekognitionImage


class RekognitionSearchUsersByImageRequest(BaseModel):
    CollectionId: StrictStr
    Image: RekognitionImage
    UserMatchThreshold: StrictFloat | StrictInt | None = None
    MaxUsers: StrictInt | None = None
    QualityFilter: Literal['NONE', 'AUTO', 'LOW', 'MEDIUM', 'HIGH'] | None = None
