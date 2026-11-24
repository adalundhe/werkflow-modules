from __future__ import annotations
from pydantic import BaseModel
from .rekognition_s3_object import RekognitionS3Object


class RekognitionMediaAnalysisInput(BaseModel):
    S3Object: RekognitionS3Object | None = None
