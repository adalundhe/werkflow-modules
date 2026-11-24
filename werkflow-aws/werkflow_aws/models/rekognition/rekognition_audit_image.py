from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_s3_object import RekognitionS3Object


class RekognitionAuditImage(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Bytes: StrictBytes | Any | None = None
    S3Object: RekognitionS3Object | None = None
    BoundingBox: RekognitionBoundingBox | None = None
