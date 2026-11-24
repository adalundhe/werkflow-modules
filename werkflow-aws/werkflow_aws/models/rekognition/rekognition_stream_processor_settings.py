from __future__ import annotations
from pydantic import BaseModel
from .rekognition_connected_home_settings import RekognitionConnectedHomeSettings
from .rekognition_face_search_settings import RekognitionFaceSearchSettings


class RekognitionStreamProcessorSettings(BaseModel):
    FaceSearch: RekognitionFaceSearchSettings | None = None
    ConnectedHome: RekognitionConnectedHomeSettings | None = None
