from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_ground_truth_manifest import RekognitionGroundTruthManifest


class RekognitionDatasetSource(BaseModel):
    GroundTruthManifest: RekognitionGroundTruthManifest | None = None
    DatasetArn: StrictStr | None = None
