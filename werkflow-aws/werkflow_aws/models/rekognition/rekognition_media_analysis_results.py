from __future__ import annotations
from pydantic import BaseModel
from .rekognition_media_analysis_model_versions import RekognitionMediaAnalysisModelVersions
from .rekognition_s3_object import RekognitionS3Object


class RekognitionMediaAnalysisResults(BaseModel):
    S3Object: RekognitionS3Object | None = None
    ModelVersions: RekognitionMediaAnalysisModelVersions | None = None
