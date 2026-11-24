from __future__ import annotations
from pydantic import BaseModel
from .rekognition_asset import RekognitionAsset


class RekognitionTrainingData(BaseModel):
    Assets: list[RekognitionAsset] | None = None
