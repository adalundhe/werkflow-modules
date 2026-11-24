from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_image import RekognitionImage


class RekognitionCompareFacesRequest(BaseModel):
    SourceImage: RekognitionImage
    TargetImage: RekognitionImage
    SimilarityThreshold: StrictFloat | StrictInt | None = None
    QualityFilter: Literal['NONE', 'AUTO', 'LOW', 'MEDIUM', 'HIGH'] | None = None
