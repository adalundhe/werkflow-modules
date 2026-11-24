from __future__ import annotations
from pydantic import BaseModel
from .rekognition_ground_truth_manifest import RekognitionGroundTruthManifest


class RekognitionAsset(BaseModel):
    GroundTruthManifest: RekognitionGroundTruthManifest | None = None
