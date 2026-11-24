from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .rekognition_asset import RekognitionAsset


class RekognitionTestingData(BaseModel):
    Assets: list[RekognitionAsset] | None = None
    AutoCreate: StrictBool | None = None
